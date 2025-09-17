#!/bin/bash

python3 -m venv locationenv
source locationenv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "Virtual environment setup complete"
echo "Activate venv by running: source locationenv/bin/activate"
