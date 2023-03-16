# Investigating artist and style mentions in Diffusion Model prompts

This is the repo for my digital humanities project, the final report is availible [here](report.pdf)

The project explores stable diffusion prompts and investigaes how artists are mentioned by users.

## Datasets

### Prompt Dataset

The project used a dataset of stable diffusion prompts. This dataset is available at [Huggingface](https://huggingface.co/datasets/poloclub/diffusiondb/blob/main/metadata-large.parquet). The most recent version of this dataset was downloaded ([Commit 1622615f9b0b2a964ec82da0a63b4b20982243ea](https://huggingface.co/datasets/poloclub/diffusiondb/commit/1622615f9b0b2a964ec82da0a63b4b20982243ea)).


:heavy_exclamation_mark: The file metadata-large.parquet has to be downloaded separately and placed in the sources folder.

### Artist Dataset

A dataset of artists is used in this project, the original dataset has been saved to [sources](sources/Image Synthesis Style Studies Database (The List).xlsx). This datset was downloaded from [here](https://docs.google.com/spreadsheets/d/14xTqtuV3BuKDNhLotB_d1aFlBGnDJOY0BRXJ8-86GpA/edit#gid=0).

The dataset was then modified for the purpose of this project, the modified version is available in this repo [here](sources/artist_info.csv).




## Notebooks

The motebooks and code of this project are available in the notebooks_and_code directory.
The notebooks in there were used for producing the results and images of the project.
The Images are automatically saved to the images folder.


Notebooks and Python files with a leading underscore did not directly contribute to the project. Most of these notebooks were used in the exploratory phase of this project. Different methodologies were explored in thee playbooks.

:heavy_exclamation_mark: The Preprocessing.ipynb playbook has to be executed first, it creates files that are used by the other playbooks.

## Installation Instructions

The notebooks require a Jupyter environment with the packages listed in requirements.txt installed.

:heavy_exclamation_mark: The **Prompt Dataset** also has to be downloaded before running the code, see readme section **Prompt Dataset**.


## other repo content

### Moritz

Playbooks written by Moritz

### dokumente

Documents created together by Moritz Weinrich and I

### ausarbeitung

ausarbeitung contains the files necessary to build the report using Latex.

### results

some playbooks save result dataframes to this directory