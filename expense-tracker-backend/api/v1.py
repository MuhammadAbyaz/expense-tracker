from fastapi import APIRouter
from ..routers import user


router = APIRouter(prefix="/v1")
router.include_router(user.router)
