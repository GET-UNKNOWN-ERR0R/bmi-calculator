@echo off

:: Display a message
echo Running BMI Calculator...

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to run this script.
    exit /b
)

:: Run the Python script
python bmi_calculator.py
