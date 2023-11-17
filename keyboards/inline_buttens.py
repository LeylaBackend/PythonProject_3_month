from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire 🧑‍💻👨‍💻",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Registration 👀",
        callback_data="registration"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    return markup


async def questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    Backend_button = InlineKeyboardButton(
        "Backend 🌑",
        callback_data="Backend"
    )
    Frontend_button = InlineKeyboardButton(
        "Frontend 🌕",
          callback_data="Frontend"
    )
    markup.add(Backend_button)
    markup.add(Frontend_button)
    return markup
