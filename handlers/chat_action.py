import datetime
import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_buttens import start_keyboard
from const import START_MENU
from profanity_check import predict, predict_prob


async def chat_messages(message: types.Message):
    db = Database()
    print(message)
    if message.chat.id == -4099855336:
        ban_word_predict_prod = predict_prob([message.text])
        user = db.sql_inserts_ban_list(telegram_id=message.from_user.id, )
        print(user)
        if ban_word_predict_prod > 0.1:
            await message.delete()
            # await bot.delete_message(
            #     chat_id=message.chat.id,
            #     message_id=message.message_id
            # )
            user = db.sql_select_ban_list(
                telegram_id=message.from_user.id,
            )
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"User: {message.from_user.id} {message.from_user.first_name}\n"
                     f"Don't be rude in chat\n"
                     f"In third time you will be banned"
            )
            print(user)
            count = None
            try:
                count = user['count']
            except TypeError:
                pass
            if not user:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Banned: {message.from_user.first_name}")
                db.sql_inserts_ban_list(
                    telegram_id=message.from_user.id
                )
            elif count >= 3:
                await bot.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.from_user.id,
                    # until_date=datetime.datetime.now() + datetime.timedelta(minutes=10)
                )
            elif user:
                db.sql_update_ban_user_count(
                    telegram_id=message.from_user.id
                )
    else:
        await message.reply(
            text="There is no such command!"
        )


# db.sql_inserts_ban_list(
#     telegram_id=message.from_user.id
# )


#         await message.reply(
#             text="Hello!"
#     )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_messages)
