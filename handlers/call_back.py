import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttens import questionnaire_keyboard
from scraping.anime_scraper import ServiceOScrapper


async def start_questioner_call(call: types.CallbackQuery):
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


async def anime_scraper_call(call: types.CallbackQuery):
    scraper = ServiceOScrapper()
    data = scraper.parse_data()
    plus_url = scraper.PLUS_URL
    for url in data[1:6]:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"{plus_url}{url}"
        )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questioner_call,
                   lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(backend_call,
                   lambda call: call.data == "Backend")
    dp.register_callback_query_handler(frontend_call,
                   lambda call: call.data == "Frontend")
    dp.register_callback_query_handler(anime_scraper_call,
                   lambda call: call.data == "anime_serial")
