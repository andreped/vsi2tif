#!/bin/bash
isort --sl vsi2tif
black --line-length 120 vsi2tif
flake8 vsi2tif
