#!/bin/sh
cd $(cd "$(dirname "$0")" && pwd)

# Ref. https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?highlight=yml#updating-an-environment
conda env update --prefix ./.conda --file environment.yml  --prune
