from dotenv import dotenv_values
from lib.database.db import connect_to_db

config = dotenv_values(".env")
if config["DB_URL"] and config["DB_NAME"]:
    client = connect_to_db(config["DB_URL"])
    db = client.expense_tracker
    expense_data = [{"name":"rent","amount":12,"category":"home"},{"name":"other","amount":150,"category":"personal"}]
    expenses = db.expenses.insert_many(doc for doc in expense_data)
    user_data = [{"username":"Abyaz","email":"test@gmail.com","password":"LOL","expenses":[expenses.inserted_ids[0]]},{"username":"Hasham","email":"test2@gmail.com","password":"LOL2","expenses":[expenses.inserted_ids[1]]}]
    db.users.insert_many(doc for doc in user_data)
    client.close()
else:
    print("Error Occurred")
