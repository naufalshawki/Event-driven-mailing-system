#!/bin/sh
export PYTHONUNBUFFERED=true
pip3 install -r requirements.txt
python consumer_script/mailing.py