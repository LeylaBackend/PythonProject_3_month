import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttens import questionnaire_keyboard

async def start_questionere_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Backend or Frontend?",
        reply_markup=await questionnaire_keyboard()
    )

async def backend_call(call: types.CallbackQuery):
    Database().sql_inserts_poll_votes(telegram_id=call.from_user.id,
                                      answer='BACKEND')
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You have chosen a Backend Developer 🎉",
    )

async def frontend_call(call: types.CallbackQuery):
    Database().sql_inserts_poll_votes(telegram_id=call.from_user.id,
                                      answer='FRONTEND')
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You have chosen a Frontend Developer 🎉",
    )

def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionere_call,
                   lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(backend_call,
                   lambda call: call.data == "Backend")
    dp.register_callback_query_handler(frontend_call,
                   lambda call: call.data == "Frontend")