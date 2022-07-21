from database.tools.base_tools import BaseTools


class IncomesTools(BaseTools):
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
