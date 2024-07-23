from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu():
    return (InlineKeyboardBuilder().
            button(text='💱 Курс валют', callback_data='rates').
            button(text='ℹ️ Информация', callback_data='info').
            button(text='👤 Написать кандидату', url='https://t.me/whytek')).adjust(2).as_markup()


def back_btn(callback):
    return InlineKeyboardBuilder().button(text='↩️ Назад', callback_data=callback).as_markup()
