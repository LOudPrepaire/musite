import warnings
import re
import os
import yaml
import boto3
import logging
import json
import sys
import tempfile
import botocore.exceptions
from src import musite

# Suppress warnings from musite
warnings.filterwarnings("ignore", category=UserWarning, module="musite")

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load configuration from YAML file
try:
    with open(os.path.join(os.getcwd(), "config.yaml"), "r") as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    logger.error("Configuration file 'config.yaml' not found in current directory.")
    sys.exit(1)
except yaml.YAMLError as e:
    logger.error(f"Error parsing config.yaml: {e}")
    sys.exit(1)

def download_from_s3(local_file: str, bucket: str, object_key: str) -> None:
    """Download a file from S3 to the specified local path."""
    s3 = boto3.client('s3')
    logger.info(f"Downloading s3://{bucket}/{object_key} to {local_file}")
    try:
        s3.download_file(bucket, object_key, local_file)
    except botocore.exceptions.ClientError as e:
        logger.error(f"Failed to download from S3: {e}")
        raise

def upload_to_s3(local_file: str, bucket: str, object_key: str) -> None:
    """Upload a file to S3 from the specified local path."""
    s3 = boto3.client('s3')
    logger.info(f"Uploading {local_file} to s3://{bucket}/{object_key}")
    try:
        s3.upload_file(local_file, bucket, object_key)
    except botocore.exceptions.ClientError as e:
        logger.error(f"Failed to upload to S3: {e}")
        raise

def process_musite_output(musite_output: str, res_number: int) -> list:
    """Process musite output and extract top-scoring residues."""
    try:
        scores = [
            {
                "resNumber": line.split('\t')[0],
                "score": float(re.findall(r":(.*)\t", line)[0])
            }
            for line in musite_output.split('\n')
            if re.findall(r"\t", line)
        ]
        sorted_scores = sorted(scores, key=lambda x: x["score"], reverse=True)
        return sorted_scores[:res_number]
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error parsing musite output: {e}")

def main(s3_input_key: str, s3_output_key: str, s3_bucket: str) -> None:
    """Process protein sequence data, compute musite scores, and upload results to S3."""
    try:
        if not all([s3_input_key, s3_bucket, s3_output_key]):
            raise ValueError("All command-line arguments (INPUT_KEY, OUTPUT_KEY, BUCKET) must be provided.")

        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = os.path.join(temp_dir, "sequence.json")
            output_file = os.path.join(temp_dir, "output.json")

            # Download input file
            download_from_s3(input_file, s3_bucket, s3_input_key)
            logger.info("Input file downloaded successfully")

            # Load and validate input data
            with open(input_file, 'r') as f:
                protein_data = json.load(f)
            required_keys = ['seq', 'resNumber']
            if not all(k in protein_data for k in required_keys):
                raise ValueError(f"JSON data must contain {required_keys} keys")
            if not isinstance(protein_data['resNumber'], int) or protein_data['resNumber'] <= 0:
                raise ValueError("resNumber must be a positive integer")

            # Process sequence with musite
            model_prefix = os.path.join(os.getcwd(), config['Paths']['modelprefix'])
            musite_result = musite.cal_musit(seq=protein_data["seq"], model_prefix=model_prefix)
            if not musite_result or not musite_result[0]:
                raise ValueError("Musite computation returned empty or invalid results")

            # Extract and sort top residues
            output = process_musite_output(musite_result[0], protein_data["resNumber"])
            logger.info(f"Processed {len(output)} top-scoring residues")

            # Write and upload output
            with open(output_file, 'w') as f:
                json.dump({"residue": output}, f, indent=4)
            upload_to_s3(output_file, s3_bucket, s3_output_key)
            logger.info("Output file uploaded successfully")

    except Exception as e:
        logger.error(f"Script failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python app.py <INPUT_KEY> <OUTPUT_KEY> <BUCKET>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])