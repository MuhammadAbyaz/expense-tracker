from fastapi import APIRouter

from ..repositories.user_repository import UserRepository


router = APIRouter()
user_repository = UserRepository()

@router.get("/{id}/expenses")
def all_expenses(id:str):
    return user_repository.find_expenses(id)
@router.get("/{user_id}/expense/{id}")
def get_expense_by_id(user_id:str,id:str):
    return user_repository.find_expense_by_id(user_id,id)

