#!/bin/bash

virtualenv --python=/usr/local/bin/python3.7 venv
export CHROME_DRIVER_PATH=''
source ./venv/bin/activate && pip install behave selenium allure-behave && behave -f allure_behave.formatter:AllureFormatter -o ./reports ./features

