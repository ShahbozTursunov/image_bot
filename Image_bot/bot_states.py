from aiogram.dispatcher.filters.state import State, StatesGroup


class UserStates(StatesGroup): #
    get_img = State()

    mailing = State()