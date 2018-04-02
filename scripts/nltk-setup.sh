#!/bin/bash
set -e
SOMETHING="a thing"
if [ ! -d "nltk-env" ]; then
    virtualenv -p python2.7 nltk-env
fi
source nltk-env/bin/activate
pip install -r nltk-requirements.txt

