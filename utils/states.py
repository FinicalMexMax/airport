from aiogram.fsm.state import State, StatesGroup


class FormFlights(StatesGroup):
    where_from = State()
    where = State()
    there = State()
    back = State()


class FromReg(StatesGroup):
    full_name = State()
    date_of_birth = State()
    