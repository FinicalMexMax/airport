from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.builders import inline_builder


router = Router()


@router.callback_query(F.data == 'profile')
async def profile(query: CallbackQuery) -> None:
    await query.message.edit_text(
        text='profile',
        reply_markup=inline_builder(
            'Back',
            'main_back'
        )
    )


@router.callback_query(F.data == 'flights')
async def flights(query: CallbackQuery) -> None:
    await query.message.edit_text(
        text='От куда?',
        reply_markup=inline_builder(
            ['Отправить геолокацию', 'Back'],
            'main_back',
            sizes=1
        )
    )


@router.callback_query(F.data == 'support')
async def support(query: CallbackQuery) -> None:
    await query.message.edit_text(
        text='support',
        reply_markup=inline_builder(
            'Back',
            'main_back'
        )
    )


# @router.callback_query(F.data == 'main_back')
# async def main_back(query: CallbackQuery) -> None:
#     await query.message.edit_text('')


# @router.callback_query(F.data == '')
# async def (query: CallbackQuery) -> None:
#     await query.message.edit_text('')