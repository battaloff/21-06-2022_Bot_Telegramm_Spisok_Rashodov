import sqlite3


def connect_database():
    connection = sqlite3.connect("DataBase.sqlite")
    cursor = connection.cursor()
    return connection, cursor


class InitDB:
    def __init__(self):
        self.connection, self.cursor = connect_database()

    def ___create_users_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(30) NOT NULL,
        chat_id INTEGER NOT NULL UNIQUE
        )""")

    def __create_incomes_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS incomes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id),
        income DECIMAL(9, 2) DEFAULT 0,
        categories VARCHAR (30) NOT NULL UNIQUE,
        date_time DATETIME NOT NULL
        )""")

    def __create_expenses_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER REFERENCES users(id),
        expense DECIMAL(9, 2) DEFAULT 0,
        categories VARCHAR (30) NOT NULL UNIQUE,
        date_time DATETIME NOT NULL
        )""")

    def start(self):
        self.___create_users_table()
        self.__create_incomes_table()
        self.__create_expenses_table()

        self.connection.commit()
        self.connection.close()


if __name__ == "__main__":
    InitDB().start()
