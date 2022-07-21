from .user_tools import UserTools
from .expenses_tools import ExpenseTools
from .incomes_tools import IncomesTools


class DBTools:
    def __init__(self):
        self.user_tools: UserTools = UserTools()
        self.incomes_tools: IncomesTools = IncomesTools()
        self.expenses_tools: ExpenseTools = ExpenseTools()
