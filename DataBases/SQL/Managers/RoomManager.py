from Postgresdb import PostgresInterface, logger

class RoomManager(PostgresInterface):
    async def add_room(self, name):
        await super().make_execute_with_singletoncheck(
            "SELECT * FROM rooms WHERE name = %s;", [name],
            "INSERT INTO rooms (name) VALUES (%s);", [name]
        )
        logger.info("Room is added")