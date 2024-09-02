#!/bin/bash
isort --check --sl -c vsi2tif
if ! [ $? -eq 0 ]
then
  echo "Please run \"sh shell/format.sh\" to format the code."
  exit 1
fi
echo "no issues with isort"
flake8 vsi2tif
if ! [ $? -eq 0 ]
then
  echo "Please fix the code style issue."
  exit 1
fi
echo "no issues with flake8"
black --check --line-length 120 vsi2tif
if ! [ $? -eq 0 ]
then
  echo "Please run \"sh shell/format.sh\" to format the code."
    exit 1
fi
echo "no issues with black"
echo "linting success!"
