from database.tools.base_tools import BaseTools


class ExpenseTools(BaseTools):
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
        WHERE user_id =? AND date_time >= "2022-07-21"
        """, (user_id,))
        expenses_by_year: list = self.cursor.fetchone()[0]
        self.connection.close()
        return expenses_by_year

