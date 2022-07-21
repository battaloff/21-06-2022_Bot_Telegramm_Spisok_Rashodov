from database import connect_database


class _BaseTools:
    def __init__(self):
        self.connection, self.cursor = connect_database()


class _UserTools(_BaseTools):

    def register_user(self, full_name: str, chat_id: int) -> None:
        try:
            self.cursor.execute("""INSERT INTO users (full_name, chat_id)
            VALUES (?,?)
            """, (full_name, chat_id))
        except:
            pass
        else:
            self.connection.commit()
        finally:
            self.connection.close()

    def get_user_id(self, chat_id: int) -> int:
        self.cursor.execute("""SELECT id
        FROM users
        WHERE chat_id = ?
        """, (chat_id,))
        user_id: int = self.cursor.fetchone()[0]
        self.connection.close()
        return user_id


class _IncomesTools(_BaseTools):
    def add_income(self, user_id: int, income: float, date_time: str) -> bool:
        status_income_add = False
        try:
            self.cursor.execute("""INSERT INTO incomes 
            (user_id, income, date_time)
            VALUES (?, ?, ?)
            """, (user_id, income, date_time))
        except:
            pass
        else:
            status_income_add = True
            self.connection.commit()
        finally:
            self.connection.close()
            return status_income_add

    def get_incomes_by_user(self, user_id: int) -> list:
        self.cursor.execute("""SELECT SUM (income)
        FROM incomes
        WHERE user_id = ?
        """, (user_id,))
        income: list = self.cursor.fetchone()[0]
        self.connection.close()
        return income

    def get_incomes_by_datetime_and_user_id(self, user_id: int, date_time: str):
        self.cursor.execute("""SELECT SUM (income)
        FROM incomes
        WHERE user_id =? AND date_time = ?
        """, (user_id, date_time))
        income_by_dt_and_user_id: list = self.cursor.fetchall()[0]
        self.connection.close()
        return income_by_dt_and_user_id

    def get_incomes_by_year(self, user_id: int, date_time: str):
        self.cursor.execute("""SELECT SUM (income)
        FROM incomes
        WHERE date>= '2022-01-01' AND date < 'now'
        """, (user_id, date_time))
        income_by_dt_and_user_id: list = self.cursor.fetchone()[0]
        self.connection.close()
        return income_by_dt_and_user_id


class _ExpenseTools(_BaseTools):
    def add_expense(self, user_id: int, expense: float, categories: str, date_time: str) -> bool:
        status_expense_add = False
        try:
            self.cursor.execute("""INSERT INTO expenses 
            (user_id, expense, categories, date_time)
            VALUES (?, ?, ?, date("now"))
            """, (user_id, expense, categories, date_time))
        except:
            pass
        else:
            status_expense_add = True
            self.connection.commit()
        finally:
            self.connection.close()
            return status_expense_add

    def get_expense_by_user(self, user_id: int) -> list:
        self.cursor.execute("""SELECT SUM (expense)
        FROM expenses
        WHERE user_id = ?
        """, (user_id,))
        expense: list = self.cursor.fetchone()[0]
        self.connection.close()
        return expense

    def get_expenses_by_datetime_and_user(self, user_id: int, date_time: str):
        self.cursor.execute("""SELECT SUM (expense)
        FROM expenses
        WHERE user_id =? AND date_time = ?
        """, (user_id, date_time))
        expense_by_dt_and_user_id: list = self.cursor.fetchall()[0]
        self.connection.close()
        return expense_by_dt_and_user_id

    def get_expenses_by_year(self, user_id: int):
        self.cursor.execute("""SELECT SUM (expense)
        FROM expenses
        WHERE date_time = "2022-07-21"
        """, (user_id,))
        expenses_by_year: list = self.cursor.fetchall()
        self.connection.close()
        return expenses_by_year


class DBTools:
    def __init__(self):
        self.user_tools: _UserTools = _UserTools()
        self.incomes_tools: _IncomesTools = _IncomesTools()
        self.expenses_tools: _ExpenseTools = _ExpenseTools()
