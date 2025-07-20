import asyncpg
from contextlib import asynccontextmanager
import logging
from SubOOPClass.singeltonClass import SingletonMeta

logging.basicConfig(
    level=logging.INFO,
    filename="../DBlogging.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("PostgresDB")

class ConnectionToDB:
    def __init__(self, pool):
        self.conn_pool = pool

    @classmethod
    async def create(cls, conn_params):
        try:
            pool = await asyncpg.create_pool(
                min_size=20,
                max_size=30,
                dsn=conn_params,
                command_timeout=5,
                server_settings={
                    'statement_timeout': '5000',
                    'idle_in_transaction_session_timeout': '10000'
                }
            )
            logger.info("Successfully connected to database")
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            raise
        return cls(pool)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logger.error(f"Exception occurred: {exc_val}")
        return False

    def close(self):
        if self.conn_pool and not self.conn_pool.closed:
            self.conn_pool.closeall()
            logger.info("DB connection pool closed")

    @asynccontextmanager
    async def connection(self):
        conn = None
        try:
            conn = await self.conn_pool.acquire()
            yield conn
        except Exception as e:
            logger.error(f"DB error: {e}")
            raise
        finally:
            if conn:
                await self.conn_pool.release(conn)

class PostgresInterface(metaclass=SingletonMeta):
    def __init__(self, connection):
        self.Connection = connection

    @classmethod
    async def create(cls):
        conn = await ConnectionToDB.create("postgresql://admin:1234@127.0.0.1:5432/messanger")
        return cls(conn)

    async def make_execute(self, base_exec: str, base_args: list) -> None:
        async with self.Connection.connection() as conn:
            async with conn.transaction():
                await conn.execute(base_exec, *base_args)

    async def make_execute_with_singletoncheck(self, check_exec:str, check_args:list, base_exec:str, base_args:list) -> bool:
        async with self.Connection.connection() as conn:
            async with conn.transaction():
                await conn.execute(check_exec, *check_args)
                if not conn.fetchrow() is None:
                    await conn.execute(base_exec, *base_args)
                    return True
        return False

