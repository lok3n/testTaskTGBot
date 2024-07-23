from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from utils.keyboards import main_menu

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: Message):
    await message.delete()
    await message.answer(f'Приветствую, {message.from_user.full_name}! Вы находитесь в главном меню',
                         reply_markup=main_menu())


@start_router.callback_query(F.data == 'main')
async def start_handler_cb(callback: CallbackQuery):
    await callback.message.edit_text(f'Приветствую, {callback.from_user.full_name}! Вы находитесь в главном меню',
                                     reply_markup=main_menu())
