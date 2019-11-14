#!/bin/bash

cd <source_dir>

./build.sh

python TestArithmetic_Operations.py

./Packagescript.sh <source_dir> <path/BOM.txt>

./cleanup.sh <source_dir>
