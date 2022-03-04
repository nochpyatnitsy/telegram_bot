@echo off 

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN = your token

python bot_telegram.py

pause 
