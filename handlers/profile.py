import sqlite3

from aiogram import types, Dispatcher
from config import bot
from const import USER_FORM_TEXT
from database.sql_commands import Database
from keyboards.inline_buttens import like_dislike_keyboard
import random
import re

async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_user_form(
        telegram_id=call.from_user.id
    )
    print(profile)
    with open(profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=USER_FORM_TEXT.format(
                nickname=profile['nickname'],
                biography=profile['biography'],
                geolocation=profile['geolocation'],
                gender=profile['gender'],
                age=profile['age'],
            ),
        )

async def random_profiles_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_all_user_form()
    random_profile = random.choice(profiles)
    with open(random_profile["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=USER_FORM_TEXT.format(
                nickname=random_profile['nickname'],
                biography=random_profile['biography'],
                geolocation=random_profile['geolocation'],
                gender=random_profile['gender'],
                age=random_profile['age'],
            ),
            reply_markup=await like_dislike_keyboard(
                owner_telegtam_id=random_profile['telegram_id']
            )
        )

async def like_dislike_call(call: types.CallbackQuery):
    print(call.data)
    owner = re.sub("liked_", "", call.data)
    try:
        db = Database()
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You already liked this photo"
        )
    finally:
        await call.message.delete()
        await random_profiles_call(call=call)

def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_profiles_call,
        lambda call: call.data == "another_profiles"
    )
    dp.register_callback_query_handler(
        like_dislike_call,
        lambda call: "liked_" in call.data
    )