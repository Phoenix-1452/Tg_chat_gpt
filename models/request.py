import asyncpg
import asyncio
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


async def connect_to_db():
    params = {
        "host": DB_HOST,
        "port": DB_PORT,
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PASS
    }

    # Подключаемся к базе данных
    conn = await asyncpg.connect(**params)

    return conn


async def main():
    conn = await connect_to_db()

    result = await conn.fetch("SELECT * FROM users")
    print(result)

    await conn.close()


asyncio.run(main())


