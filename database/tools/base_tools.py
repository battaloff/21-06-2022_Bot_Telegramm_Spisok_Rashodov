from database.utils import connect_database


class BaseTools:
    def __init__(self):
        self.connection, self.cursor = connect_database()
