#!/bin/bash

echo "Running BMI Calculator..."

if command -v python3 &>/dev/null; then
 
    python3 bmi_calculator.py
else
    echo "Python3 is not installed. Please install Python3 to run this script."
fi
