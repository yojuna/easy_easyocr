# README

Thin wrapper around the EasyOCR library, which handles urls and images on disk and outputs the OCR'd text, on top of the recognized text, using openCV.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Aknowledgements](#ackowledgements)
- [TODO's](#todo's)

## Installation / Setup

```sh
pip install opencv-python
pip install easyocr
```

NOTE: It would be prudent to create a virtual environment that pulls system site packages if you already have pytorch installed and configured as the easyocr install starts pulling and installing torch (~700mb) in a new virtualenv

#### To use the virtualenv kernel in jupyter

activate the environment, then
```sh
pip install --user ipykernel
python -m ipykernel install --user --name=myenv
```
substituting --name=myenv with your virtualenv name and then select the kernel as required.

Better explained over here: https://anbasile.github.io/posts/2017-06-25-jupyter-venv/

## Usage

Either use the self explanatory and commented jupyter notebook 'ocr_reader.ipynb' or the python program using the cli.

For CLI usage:
```sh
$ python easy_easyocr.py --is_url True --image "https://example.com/exampleimage" --langs "en,tr" --use_gpu True
```
Flags:

```
"-u", "--is_url", type=bool, default=False, help="if image parameter is an url or filepath"
"-i", "--image", required=True, help="path to input image to be OCR'd"
"-l", "--langs", type=str, default="en", help="comma separated list of languages to OCR"
"-g", "--use_gpu", type=bool, default=False, help="whether or not GPU should be used"
```
For language codes, refer the EasyOCR github repo.

## Acknowledgements

Inspired by this article by Adrian Rosebrock of PyImageSearch [https://www.pyimagesearch.com/2020/09/14/getting-started-with-easyocr-for-optical-character-recognition/]
also, obvious credits to JaidedAI for this amazingly stable library [https://github.com/JaidedAI/EasyOCR]

## TODO's

1. Convert to a web app
