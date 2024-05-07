<<<<<<< HEAD
# Dev



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin http://ec2-18-200-126-211.eu-west-1.compute.amazonaws.com/personal/milad/dev.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](http://ec2-18-200-126-211.eu-west-1.compute.amazonaws.com/personal/milad/dev/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
=======
# PTM prediction

We provide 13 different models for PTM site predictions and customized model training that enables users to train models by their own data. 
Users can find the models in the folder of MusiteDeep/models. 
##### Installation

  - Installation has been tested in Ubuntu 16.04.5 LST and Mac OS HighSierra with python 3.5.2: 
You can install the dependent packages by the following commands:
    ```sh
    sudo apt-get install -y python3.5 python3-pip
    python3 -m pip install numpy 
    python3 -m pip install scipy
    python3 -m pip install scikit-learn
    python3 -m pip install pillow
    python3 -m pip install h5py
    python3 -m pip install pandas
    python3 -m pip install keras==2.2.4
    python3 -m pip install tensorflow==1.12.0 (or install the GPU supported tensorflow by pip3 install tensorflow-gpu==1.12.0 refer to https://www.tensorflow.org/install/ for instructions)
    ```
    Download the stand-alone tool by:
    ```sh
    git clone https://github.com/duolinwang/MusiteDeep_web
    ```
##### Running on GPU or CPU
>If you want to use GPU, you also need to install [CUDA]( https://developer.nvidia.com/cuda-toolkit) and [cuDNN](https://developer.nvidia.com/cudnn); refer to their websites for instructions. 
CPU is only suitable for prediction not training. 

##### For general users who want to perform PTM site prediction by our provided model :
go to the MusiteDeep folder which contains the predict_multi_batch.py
```sh
python3 predict_multi_batch.py -input [custom prediction data in FASTA format] -output [custom specified prefix for the prediction results] -model-prefix [prefix of pre-trained model] 
```
For details of the parameters, use the -h or --help parameter.

The -model-prefix can be "models/XX/", here XX represents one pre-trained model in the folder of "MusiteDeep/models/". To predict for multiple PTMs, use ";" to separate the prefixes of different pre-trained models.
For example, to predict for phosphotyrosine and methyllysine simultaneously, run the following command:
```sh
python3 predict_multi_batch.py -input testdata/Phosphorylation/Y/test_allspecies_sequences.fasta -output test/output  -model-prefix "models/Phosphotyrosine;models/Methyllysine";

or

python3 predict_multi_batch.py -input testdata/Phosphorylation/Y/test_allspecies_sequences.fasta -output test/output  -model-prefix "models/Phosphotyrosine;Methyllysine";
```

##### For advanced users like to perform training and prediction by using their own data
Because we used ensemble models by two deep-learning architectures, two types of models need to be trained: one is the CNN model [1] trained by train_CNN_10fold_ensemble.py, and the other is the capsule model [2] trained by train_capsnet_10fold_ensemble.py. To train a customized predictor, users can run the following commands and replace with their own data and parameters.
```sh
python3 train_CNN_10fold_ensemble.py -load_average_weight -balance_val -input [custom training data in FASTA format] -output [folder for the output models] -checkpointweights [folder for the intermediate checkpoint files] -residue-types [custom specified residue types]

python3 train_capsnet_10fold_ensemble.py -load_average_weight -balance_val -input [custom training data in FASTA format] -output [folder for the output model] -checkpointweights [folder for the intermediate checkpoint files] -residue-types [custom specified residue types]
```
The training data should be in the FASTA format. Residues followed by "#" indicates the positive sites, residues in the custom specified residue types but without "#" are considered as the negative sites. Tje -residue-types parameter indicates the potential modification residue types that this model focuses on. Multiple types of residues are separated with ','. And all the residues specified by this parameter will be trained in one predictor. For details of other parameters, use the -h or --help parameter.
##### Examples of commands used to train our provided models:
 For Phosphoserine_Phosphothreonine:

 ```sh
 python3 train_CNN_10fold_ensemble.py -load_average_weight -balance_val -input "testdata/Phosphorylation/ST/train_allspecies_sequences_annotated.fasta" -output "./models_test/Phosphoserine_Phosphothreonine/CNNmodels/" -checkpointweights "./models_test/Phosphoserine_Phosphothreonine/CNNmodels/" -residue-types S,T -nclass=1 -maxneg 30
 python3 train_capsnet_10fold_ensemble.py -load_average_weight -balance_val -input "testdata/Phosphorylation/ST/train_allspecies_sequences_annotated.fasta" -output "./models_test/Phosphoserine_Phosphothreonine/capsmodels/" -checkpointweights "./models_test/Phosphoserine_Phosphothreonine/capsmodels/" -residue-types S,T -nclass=1 -maxneg 30
```
 For Phosphotyrosine, we transferred the pre-trained weights from Phosphoserine_Phosphothreonine:
```sh
 python3 train_CNN_10fold_ensemble.py -load_average_weight -balance_val -inputweights ./models/Phosphoserine_Phosphothreonine/CNNmodels/model_HDF5model_fold0_class0 -input "testdata/Phosphorylation/Y/train_allspecies_sequences_annotated.fasta" -output "./models_test/Phosphotyrosine/CNNmodels/" -checkpointweights "./models_test/Phosphotyrosine/CNNmodels/" -residue-types Y -nclass=1 -maxneg 30
 python3 train_capsnet_10fold_ensemble.py -load_average_weight -balance_val -inputweights ./models/Phosphoserine_Phosphothreonine/capsmodels/model_HDF5model_fold0_class0 -input "testdata/Phosphorylation/Y/train_allspecies_sequences_annotated.fasta" -output "./models_test/Phosphotyrosine/capsmodels/" -checkpointweights "./models_test/Phosphotyrosine/capsmodels/" -residue-types Y -nclass=1 -maxneg 30
 ```
### Training and testing data are provided in the folder of MusiteDeep/testdata.
>>>>>>> cf3d208 (Merge branch 'MusiteDeep' of ec2-18-200-126-211.eu-west-1.compute.amazonaws.com into MusiteDeep)
