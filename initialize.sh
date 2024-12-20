#!/bin/bash

# Config git hub
name="$1"
email="$2"
if [ -z "$name" ] || [ -z "$email" ]; then
    echo "Usage: ./initialize.sh <your_name> <your_email> <your_task>"
    exit 1
fi

git config --global user.name "$name"
git config --global user.email "$email"

# Use conda to create environment
conda env create -f environment.yml

# Add upstream path
git remote add upstream https://github.com/tlong-ds/dseb65b_mid.git
git pull upstream main
