
from aiogram import  types ,  Dispatcher
from create_bot import dp , Bot 
from keyboards import kb_client
from aiogram.types import  ReplyKeyboardRemove 
from data_base import sqlite_db
#@dp.message_handler(commands=['start' , 'help'])
async def comands_start_command(message : types.Message):
    try:
        await Bot.send.message(message.from_user.id , 'приятного аппетита ' , reply_markup = kb_client )
        await message.delete()
    except:
        await message.reply('общение с ботом через личные сообщения , напишите ему: \n @Pizza_bot_maaaanBot ')

#@dp.message_handler(commands=['режим работы'])
async def pizza_open_command(message : types.Message):
    await Bot.send.message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')

#@dp.message_handler(commands=['расположение'])
async def pizza_place_command(message : types.Message):
    await Bot.send.message(message.from_user.id, 'СМ.Институт Культуры' )
    
#@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message : types.Message):
    await sqlite_db.sql_reading(message)


def register_handlers_client ( dp : Dispatcher):
    dp.register_message_handler(comands_start_command , commands = ['start' , 'help'])
    dp.register_message_handler(pizza_open_command , commands=['режим работы'])
    dp.register_message_handler(pizza_place_command , commands=['расположение'])
    dp.register_message_handler(pizza_menu_command , commands = ['Меню'])

    