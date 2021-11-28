#!/bin/bash

arg="init"
if [ $1 == $arg ]; then
  echo "Initiating **********"
  py -3 -m venv venv
  venv/Scripts/activate.bat
  pip install -r requirenets.txt
else
  echo "Starting fastapi app on dev ****** "
  uvicorn app.main:app --reload
fi

