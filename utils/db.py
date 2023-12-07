from aiogram import Router
import asyncpg
from os import getenv
from dotenv import load_dotenv


router = Router()


async def check_reg_user(db: asyncpg.connect, user_id: int):
    db.fetch("""
    SELECT id FROM account WHERE id = ?;
    """, (user_id)
    )


async def connect(
        dp,
        user: str, 
        password: str, 
        host: str, 
        database: str
    ):
    
    db_pool = await asyncpg.create_pool(
        user=user, 
        password=password,
        database=database, 
        host=host
    )

    dp['db'] = db_pool

    print('Connect database...')


# class ConnectDataBase:
#     async def __init__(
#         self, 
#         user: str, 
#         password: str, 
#         host: str, 
#         database: str
#     ) -> None:
        
#         self.user = user
#         self.password = password
#         self.host = host
#         self.database = database

#     async def connect(self) -> asyncpg.connect:
#         return await asyncpg.connect(
#             user=self.user, 
#             password=self.password,
#             database=self.database, 
#             host=self.host
#         )
    
#     async def close(self) -> None:
#         self.connect().close()