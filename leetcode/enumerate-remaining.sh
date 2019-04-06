#!/bin/bash

# This script looks through all of the existing directories and prints
# the ones where a Python solution exists but a C++ does not.

for DIRECTORY in $(ls)
do
  if [ -f $DIRECTORY/solution.py ] && [ ! -f $DIRECTORY/solution.cpp ]; then
    echo $DIRECTORY
  fi
done
