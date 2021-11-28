#!/bin/bash

#py -3 -m venv venv

#venv/Scripts/activate.bat

#pip install -r requirenets.txt

#uvicorn main:app --reload
arg=$1
echo "##****************************arg"
 if [ "$1" -eq  "init" ]
   then
     echo "No arguments supplied"
 else
     echo "Hello world"
 fi

