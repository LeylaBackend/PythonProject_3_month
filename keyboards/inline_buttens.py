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
    my_profile_button = InlineKeyboardButton(
        "My profile 🧩",
        callback_data="my_profile"
    )
    another_profile = InlineKeyboardButton(
        "Another profiles 👾",
        callback_data="another_profiles"
    )
    reference_menu_button = InlineKeyboardButton(
        "Reference Menu 🍪",
        callback_data="reference_menu"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    markup.add(another_profile)
    markup.add(reference_menu_button)
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

async def like_dislike_keyboard(owner_telegtam_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍",
        callback_data=f"liked_{owner_telegtam_id}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎",
          callback_data=f"dislike_{owner_telegtam_id}"
    )
    markup.add(like_button)
    markup.add(dislike_button)
    return markup

async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_button = InlineKeyboardButton(
        "Reference Link 🔗",
        callback_data="reference_link"
    )
    reference_profile_button = InlineKeyboardButton(
        "Referral Profile 👁",
        callback_data="referral_profile"
    )
    markup.add(reference_button)
    markup.add(reference_profile_button)
    return markup