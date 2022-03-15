#!/usr/bin/env bash

# sudo apt install -y mupdf-tools poppler-utils
python3 -m pip install --upgrade pip
pip3 install pytest pytest-cov pytest-github-actions-annotate-failures jupyter numpy matplotlib

# rm tests.py
wget -N https://raw.githubusercontent.com/hse-mlwp-2022/assignment3-template/main/tests.py
jupyter nbconvert --to script --output "pandas_assignment_dirty" pandas_assignment.ipynb
cat pandas_assignment_dirty.py | grep -v "^#" | grep -v "^$" | grep -v "get_ipython()" | grep -vE "(\s|=|^)input\(" > pandas_assignment.py
pytest -s tests.py