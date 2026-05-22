from Postgresdb import PostgresInterface, logger

class UserManagerFromClient(PostgresInterface):
    async def add_user(self, login, password):
        await super().make_execute_with_singletoncheck(
            "SELECT * FROM users WHERE login = %s;", [login],
            "INSERT INTO users (login, password) VALUES (%s, %s);", [login, password]
        )
        logger.info("User is added")