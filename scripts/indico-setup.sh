#!/bin/bash
set -e
if [ ! -d "indico-env" ]; then
    virtualenv -p python2.7 indico-env
fi
source indico-env/bin/activate
pip install -r indico-requirements.txt

