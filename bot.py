import asyncio
import datetime
import platform
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentType
from aiogram.types.web_app_info import WebAppInfo

from db_func import new_user

if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import config
from keyboards import *

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot)
print(f'bot is starting at {datetime.datetime.now().replace(microsecond=0)}')


@dp.message_handler(state='*', content_types=['text', 'photo', 'document'])
async def msg_text(message: types.Message, state: FSMContext):
    user_name = message.from_user.username
    if user_name != None:
        user_name = f"@{user_name}"

    msg = str(message.text)
    tlgm_id = message.from_user.id
    user_state = await state.get_state()
    new_user(tlgm_id=tlgm_id,user_name=user_name)
    text = 'Какую мебель вам нужно изготовить?'
    await bot.send_message(tlgm_id, text=text, reply_markup=main_kb())


@dp.callback_query_handler(state='*')
async def press(call: types.CallbackQuery, state: FSMContext):
    tlgm_id = call.message.chat.id
    press = call.data
    if press in ['other','wardrobe']:
        text = 'У вас есть примерное изображение мебели, которую нужно изготовить'
        kb = types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton('Да, есть',callback_data='photo_true'),
            types.InlineKeyboardButton('Пообщаться с менеджером',callback_data='dialog_manager'),
        )
        await bot.send_message(tlgm_id, text=text, reply_markup=kb)
    if press=='photo_true':
            text = 'пожалуйста пришлите изображения,  в течении 15 минут менеджер напишет вам'
            await bot.send_message(tlgm_id, text=text, reply_markup=reply_kb_main_menu())
    if press=='kitchen':
        text = 'У вас уже есть проект или чертеж будущей мебели?'
        kb = types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton('Да, есть', callback_data='photo_true'),
            types.InlineKeyboardButton('Нет, хочу узнать примерную стоимость', web_app=types.WebAppInfo(url = f'https://127.0.0.1/calc/{tlgm_id}')),
            types.InlineKeyboardButton('TEST', web_app=types.WebAppInfo(url = 'https://bigmebel-msk.ru/kalkulyator-kuhni/')),
        )
        await bot.send_message(tlgm_id, text=text, reply_markup=kb)
if __name__ == '__main__':
    executor.start_polling(dp)
