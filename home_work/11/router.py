from fastapi import APIRouter, Depends
from schema import *
from database import UserRepository


user_router = APIRouter(prefix="/users/", tags=['users'])


@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id": id}


@user_router.get('')
async def get_users() -> list[User]:
    users = await UserRepository.get_users()
    return users


@user_router.get('/{id}')
async def get_user(id):
    user = await UserRepository.add_user(id)
    return user
