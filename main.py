import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Router, Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.builders import inline_builder

from callbacks import navigation


load_dotenv()
router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == 'main_back')
async def start(message: Message | CallbackQuery) -> None:
    if isinstance(message, CallbackQuery):
        await message.message.edit_text(
            'Hello, world!',
            reply_markup=inline_builder(
                ['Профиль', 'Рейсы', 'Поддержка'],
                ['profile', 'flights', 'support']
            )
        )
        await message.answer()
    else:
        await message.answer(
            'Hello, world!',
            reply_markup=inline_builder(
                ['Профиль', 'Рейсы', 'Поддержка'],
                ['profile', 'flights', 'support']
            )
        )

async def main() -> None:
    bot = Bot(token=getenv('TOKEN'))
    dp = Dispatcher()

    dp.include_routers(
        router,
        navigation.router
    )

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())