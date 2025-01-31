import bcrypt

global salt 
salt = '$2b$12$cBQ2MOmKZbDrXkEvmiI5Ne'

class Password():
    def __init__(self):
        self.salt = salt.encode('utf-8')
    
    def getHash(self, password):
        password = password.encode('utf-8')
        hash_password = bcrypt.hashpw(
            password=password,
            salt=self.salt
        )
        return hash_password.decode('utf-8')
    