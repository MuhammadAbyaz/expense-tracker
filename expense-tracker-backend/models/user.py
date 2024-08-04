from pymongoose import Schema, Types
from typing import List,Optional

from ..models.expense import Expense

class User(Schema):
    schema_name = "users"
    username:str
    email:str
    password:str
    expenses: Optional[List[Expense]]

    def __init__(self,**kwargs):
        self.schema = {
            "username": {
                "type": Types.String,
                "required":True
            },
            "email": {
                "type": Types.String,
                "required": True
            },
            "password": {
                "type": Types.String,
                "required": True
            },
            "expenses": [{
                "type": Types.ObjectId,
                "ref": "expenses"
            }]
        }
        super().__init__(self.schema_name, self.schema, kwargs)
    @classmethod
    def to_json(cls,data):
        return {"_id":str(data["_id"]),"username":data["username"], "email":data["email"],"password":data["password"], "expenses":data["expenses"]}
