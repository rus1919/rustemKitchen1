from aiogram import types

def main_kb():
    kb = types.InlineKeyboardMarkup(row_width=2).add(
        types.InlineKeyboardButton('Кухню',callback_data='kitchen'),
        types.InlineKeyboardButton('Шкаф',callback_data='wardrobe'),
    )
    kb.add(types.InlineKeyboardButton('Другая корпусная мебель',callback_data='other'))
    kb.add(types.InlineKeyboardButton('Позвать менеджера',callback_data='manager'))
    return kb

def reply_kb_main_menu():
    return types.ReplyKeyboardMarkup(resize_keyboard=True).add(types.KeyboardButton('Главное меню'))