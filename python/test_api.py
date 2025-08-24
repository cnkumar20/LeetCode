from fastapi import FastAPI, APIRouter

app = FastAPI()

user_router = APIRouter()

@user_router.get("/users/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    """
    Retrieve user details.
    """
    return {"user_id": user_id}

app.include_router(user_router)
