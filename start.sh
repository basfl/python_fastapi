#!/bin/bash

py -3 -m venv venv

venv/Scripts/activate.bat

pip install -r requirenets.txt

uvicorn main:app --reload