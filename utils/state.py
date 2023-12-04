from aiogram.fsm.state import State, StatesGroup


class FormFlights(StatesGroup):
    where_from = State()
    where = State()

    