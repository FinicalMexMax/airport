from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.builders import inline_builder
from keyboards.reply import send_geo

from utils.states import FormFlights
from utils.geo import get_city


router = Router()


@router.callback_query(F.data == 'flights')
async def flights(query: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(FormFlights.where_from)

    await query.message.answer(
        text='От куда?',
        reply_markup=send_geo
    )


@router.message(FormFlights.where_from, F.text | F.location)
async def take_on_form_flight(message: Message, state: FSMContext) -> None:
    if message.location:
        await message.answer(
            get_info(
                lat=message.location.latitude,
                lon=message.location.longitude
            )
        )
    else:
        await state.update_data(where_from=message.text)

        print(message.text)