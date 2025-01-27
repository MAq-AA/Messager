import bcrypt
 

class Password():
    def __init__(self, salt = '$2b$12$cBQ2MOmKZbDrXkEvmiI5Ne'):
        self.salt = salt.encode('utf-8')
    
    def getHash(self, password):
        password = password.encode('utf-8')
        hash_password = bcrypt.hashpw(
            password=password,
            salt=self.salt
        )
        return hash_password.decode('utf-8')
    