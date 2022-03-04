from aiogram import types , Dispatcher
from create_bot import dp 
import json
import string 


@dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translaete(str.maketrans('' , '' , 'string.punctuation' )) for i in message.text.split(' ')}: 
        .intersection(set (json.load(open(mat.json)))) != set () :
        await message.reply ('маты запрещены ')
        await message.delete()

def register_handlers_other( dp : Dispatcher):
    dp.register_message_handker(echo_send )
