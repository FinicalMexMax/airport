from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


send_geo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Отправить геолокацию', 
                request_location=True
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

rm = ReplyKeyboardRemove()