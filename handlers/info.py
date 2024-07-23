from aiogram import F, Router
from aiogram.types import CallbackQuery
from utils.keyboards import back_btn

info_router = Router()


@info_router.callback_query(F.data == 'info')
async def info_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        '📌 Этот бот создан для прохождения собеседования на вакансию Junior Python Developer, '
        'в нём Вы можете ознакомиться с актуальным курсом валют',
        reply_markup=back_btn('main'))
