from setup import dp, bot
from db.database import check_user, add_user
from config import ROOT_USER

import os
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton, InlineKeyboardMarkup


#base_path = os.path.join(os.path.dirname(__file__), "images")

def root_menue() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text='👥 Пользователи', callback_data='root_chearch_users')
    )

def registrate() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text='➕ отправить заявку', callback_data='reg')
    )

def approve(targert) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(row_width=1).add(
        InlineKeyboardButton(text='✅ Одобрить', callback_data=f'approve_{str(targert)}'),
        InlineKeyboardButton(text='⛔ Отклонить', callback_data=f'del_approve__{str(targert)}'),
    )

@dp.message_handler(commands='start')
async def main_menu(message: types.message) -> None:
    if message.from_user.id == int(ROOT_USER):
        await bot.send_message(
            message.from_user.id,
            f"Привет, {message.from_user.username}",
            reply_markup=root_menue()
        )
    if check_user(message.from_user.id):
        await bot.send_message(
            message.from_user.id,
            f"вы находитесь в меню рассылок\n"
        )
    else:
        await bot.send_message(
            message.from_user.id,
            f"⛔ Вы не зарегистрированы в системе",
            reply_markup=registrate()
        )

@dp.callback_query_handler(text="reg")
async def about(call: types.CallbackQuery):
    await bot.delete_message(
        message_id=call.message.message_id - 1,
        chat_id=call.from_user.id
    )
    await bot.edit_message_text(
        message_id=call.message.message_id,
        chat_id=call.from_user.id,
        text="✅ Заявка отправлена!"
    )
    await bot.send_message(
        int(ROOT_USER),
        f"Вам пришла заявка на добавление в wazzup-sendler от\n@{call.from_user.username}",
        reply_markup=approve(call.from_user.id)
    )

@dp.callback_query_handler(lambda query: query.data.startswith('approve_'))
async def button_pressed_handler(query: types.CallbackQuery):
    user_id = query.data.split('_')[1]  # Получаем user_id из callback_data
    await query.answer(f'Кнопка была нажата, user_id={user_id}')\



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(main_menu)
