#!/bin/bash

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run the script in the background
LOGFILE="scraper.log"
nohup python3 main.py > "$LOGFILE" 2>&1 &
PID=$!
echo "Script is running in the background with PID $PID"
