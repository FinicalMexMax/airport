import asyncio
from os import getenv
from dotenv import load_dotenv

from aiogram import Router, Dispatcher, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import asyncpg

from keyboards.builders import inline_builder

from callbacks import navigation, flights

from utils import db as database


load_dotenv()
router = Router()


@router.message(CommandStart())
@router.callback_query(F.data == 'main_back')
async def start(message: Message | CallbackQuery, db: asyncpg.create_pool) -> None:
    await db.fetch("""
    CREATE TABLE account (
        id INT,
        name VARCHAR
    );
    """)

    if isinstance(message, CallbackQuery):
        await message.message.edit_text(
            'Хай',
            reply_markup=inline_builder(
                ['Профиль', 'Рейсы', 'Поддержка'],
                ['profile', 'flights', 'support']
            )
        )
        await message.answer()
    else:
        await message.answer(
            'Хай',
            reply_markup=inline_builder(
                ['Профиль', 'Рейсы', 'Поддержка'],
                ['profile', 'flights', 'support']
            )
        )


async def main() -> None:
    bot = Bot(token=getenv('TOKEN'))
    dp = Dispatcher()

    await database.connect(
        dp,
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        host=getenv("DB_HOST"),
        database=getenv("DB_NAME")
    )

    dp.include_routers(
        router,
        navigation.router,
        flights.router,
        database.router
    )

    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())