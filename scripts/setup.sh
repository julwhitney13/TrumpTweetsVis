#!/bin/bash
set -e
if [ ! -d "env" ]; then
    virtualenv -p python2.7 env
fi
source env/bin/activate
pip install -r requirements.txt

