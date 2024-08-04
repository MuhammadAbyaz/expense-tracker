from typing import Dict, List

from ..models.expense import Expense
from ..models.user import User


class UserRepository:
    def __init__(self) -> None:
        self.model = User()

    def save(self,model)->str:
        return model.save()

    def find_by_id(self,id:str)->Dict:
        return self.model.to_json(self.model.find_by_id(id,parse=False,populate=[{"path":"expenses"}]))

    def find_expenses(self,id:str)->List[Dict]:
        expenses = self.find_by_id(id)["expenses"]
        return [Expense.to_json(expense) for expense in expenses]

    def find_expense_by_id(self,user_id:str,expense_id:str)->Dict|None:
        expenses: List[Dict] = self.find_expenses(user_id)
        for expense in expenses:
            if expense["_id"] == expense_id:
                return expense
        return None

