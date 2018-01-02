#!/bin/bash

cd tests
PYTHONPATH=../src
python3 -m pytest
