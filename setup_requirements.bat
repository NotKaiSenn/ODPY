@echo off
@title Doctorate - Setup

set "oldVirtualEnvironmentFolder=oldEnv"
set "virtualEnvironmentFolder=env"

if exist %oldVirtualEnvironmentFolder%\ (
  echo Doing cleanup 
  rmdir /S /Q %oldVirtualEnvironmentFolder%
) else (
  echo No cleanup to do
)

call %virtualEnvironmentFolder%\scripts\activate.bat

IF '%errorlevel%' NEQ '0' (
    @REM If the virtual environment fails to activate we create it
    echo Preparing environment
    python -m venv %virtualEnvironmentFolder%
    call %virtualEnvironmentFolder%\scripts\activate.bat
    call pip install -r requirements.txt -U
)

cls
python setup_requirements.py