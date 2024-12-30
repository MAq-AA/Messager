import sqlite3

def initialSQLite3DB():
    connection = getConnectToSQLite3()
    createTabels(connection)
    return connection

def getConnectToSQLite3():
    return sqlite3.connect('my_database.db')
    
def closeConnectToSQLite3(connection):
    connection.close()

def createTabels(connection):
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id              INTEGER     PRIMARY KEY,
        username        TEXT        NOT NULL,
        password        TEXT        NOT NULL,
        email           TEXT        NOT NULL
        )
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Rooms (
        id              INTEGER     PRIMARY KEY,
        name            TEXT           
        )
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Messages (
        id              INTEGER     PRIMARY KEY,
        sender          INTEGER,
        room            INTEGER,
        textOFmessage   TEXT        NOT NULL,
        FOREIGN KEY (sender) REFERENCES USERS (id),
        FOREIGN KEY (room) REFERENCES ROOMS (id) 
        )
        ''')
    
    connection.commit()

def addUser(connection, username, email):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', 
                   (username, email))
    connection.commit()

def addMessage(connection, sender, room, text):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Messages (sender, room, text) VALUES (?, ?, ?)', 
                   (sender, room, text))
    connection.commit()

def addMessage(connection, name):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Messages (name) VALUES (?, ?, ?)', 
                   (name))
    connection.commit()     