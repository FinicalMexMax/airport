import asyncio
import asyncpg
from os import getenv
from dotenv import load_dotenv


class ConnectDataBase:
    async def __init__(
        self, 
        user: str, 
        password: str, 
        host: str, 
        database: str
    ) -> None:
        
        self.user = user
        self.password = password
        self.host = host
        self.database = database

    async def connect(self) -> asyncpg.connect:
        return await asyncpg.connect(
            user=self.user, 
            password=self.password,
            database=self.database, 
            host=self.host
        )
    
    async def close(self) -> None:
        self.connect().close()