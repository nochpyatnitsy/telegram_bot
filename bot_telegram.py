from aiogram.untils import executor 
from  create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('бот вышел в онлайн')
    sqlite_db.sql_start()


from handlers import client_side , admin_side , other

client_side.register_handlers_client(dp)
admin_side.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp , skip_updates = True , on_startup = on_startup)
