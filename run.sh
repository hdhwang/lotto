#!/bin/bash
SCRIPT_PATH=$(dirname $(realpath $0))

source $SCRIPT_PATH/venv/bin/activate
python3 $SCRIPT_PATH/lotto_statistics.py
deactivate
