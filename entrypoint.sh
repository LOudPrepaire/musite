#!/bin/bash

# Initialize Conda properly
eval "$(conda shell.bash hook)"

# Activate the FastAPI Conda environment
echo "Activating Conda environment: fastapi-service"
conda activate fastapi-service

# Check if activation was successful
if [[ $? -ne 0 ]]; then
    echo "Failed to activate Conda environment. Exiting."
    exit 1
fi


echo "Environment vars:"
env | grep -E 'INPUT|OUTPUT|BUCKET'

python3 app.py "$INPUT" "$OUTPUT" "$BUCKET" 
