import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttens import start_keyboard


async def start_button(message: types.Message):
    print(message)
    db = Database()
    try:
        db.sql_insert_users(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass
    # db = Database()
    # db.sql_inserts_poll_votes(
    #     telegram_id=message.from_user.id,
    #     answer=message.answer,
    # )
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f"Hello {message.from_user.first_name}",
        reply_markup=await start_keyboard()
    )
def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])


