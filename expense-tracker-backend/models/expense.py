from typing import Dict
from pymongoose import Schema,Types

class Expense(Schema):
    schema_name = "expenses"
    name: str
    amount: float
    category: str

    def __init__(self,**kwargs):
        self.schema = {
            "name": {
                "type": Types.String,
                "required": True,
            },
            "amount": {
                "type": Types.Number,
                "required": True
            },
            "category":{
                "type": Types.String,
                "required": True
            }
        }
        super().__init__(self.schema_name, self.schema, kwargs)
    
    @classmethod
    def to_json(cls,data)->Dict:
        return {"_id": str(data["_id"]), "name":data["name"], "amount": data["amount"], "category": data["category"]}
