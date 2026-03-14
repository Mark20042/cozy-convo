from fastapi import APIRouter, Request
from controllers import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# get current user
@router.get("/me")
async def get_current_user_route(request: Request):
    return await get_current_user(request)
