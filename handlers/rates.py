from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from utils.keyboards import back_btn
from utils.redis_storage import storage
course_router = Router()


@course_router.message(Command('rates'))
@course_router.callback_query(F.data == 'rates')
async def course_handler(callback: CallbackQuery):
    if isinstance(callback, Message): # it's for handle 2 different events (msg or cb) in 1 func
        await callback.delete()  # this not callback object, this message object
        msg = await callback.answer('⏳ Загрузка . . .')
    else:
        await callback.message.edit_text('⏳ Загрузка . . .')
        msg = callback.message
    data = storage.get_rates()
    text = '\n'.join([f'{i} - {data[i]["Name"]} - {data[i]["Value"]}₽' for i in data])
    await msg.edit_text(f'✅ Окей, вот актуальный курс!\n\n{text}'
                        '\n\nℹ️ Чтобы вернуться назад, нажми на кнопку ниже',
                        reply_markup=back_btn('main'))
