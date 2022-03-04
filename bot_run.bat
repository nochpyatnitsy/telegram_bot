@echo off 

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN = 5190257948:AAG_WyXbTTZtCBfSaxb0ZbAyw6Aukra0EcA

python bot_telegram.py

pause 
