from fastapi import APIRouter, status, Response
from models.users import UserCreate, UserLogin
from controllers import register_user, login_user, logout_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# register
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user_route(user_data: UserCreate):
    return await register_user(user_data)

# login
@router.post("/login")
async def login_user_route(credentials: UserLogin, response: Response):
    return await login_user(credentials, response)

# logout
@router.post("/logout")
async def logout_user_route(response: Response):
    return await logout_user(response)
