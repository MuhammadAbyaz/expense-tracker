from typing import Dict,Any

from ...models.expense import Expense
from ...models.user import User



schemas: Dict[str,Any] = {
    "expenses": Expense().schema,
    "users": User().schema
}
