from Postgresdb import PostgresInterface, logger
import asyncio

class MessageManager(PostgresInterface):
    async def add_message(self, author, text, room):
        await super().make_execute(
            "INSERT INTO messages (author, text, room) VALUES ($1, $2, $3);", [author, text, room]
        )
        logger.info("Message is added")

async def main():
    db = await MessageManager.create()
    for i in range(0, 1000):
        await db.add_message(64, "sdsdsd", 1)

asyncio.run(main())