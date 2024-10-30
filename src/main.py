from fastapi import FastAPI
from src.auth.authentification import fastapi_users, auth_backend
from src.auth.schemas import UserCreate, UserRead
from src.users.router import router as userRouter

app = FastAPI(title="TestApp")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(userRouter)