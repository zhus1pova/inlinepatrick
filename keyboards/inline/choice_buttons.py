
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_ZHUSIPOVASHOP, URL_lOCATION, URL_OSNAVATEL, URL_DOSTSVKA, URL_OTZYVY

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Zhusipovas' shop", callback_data=buy_callback.new(item_name="Zhusipovas' shop", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="location", callback_data="buy:location:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Osnavatel'", callback_data="buy:Osnavatel':5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Dostavka", callback_data="buy:Dostavka:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Otzyvy", callback_data="buy:Otzyvy:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="Visit", url=URL_ZHUSIPOVASHOP)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_lOCATION)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_OSNAVATEL)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_DOSTSVKA)

    ]



])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_OTZYVY)

    ]

])