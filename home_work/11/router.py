from typing import List, Sequence
from fastapi import APIRouter, Depends
from schema import *
from database import UserRepository, QuizRepository, QuizOrm, UserOrm

user_router = APIRouter(prefix="/users/", tags=['users'])
quiz_router = APIRouter(prefix="/quizzes/", tags=['quizzes'])
question_router = APIRouter(prefix="/questions/", tags=['questions'])


@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id": id}


@user_router.get('')
async def get_users() -> Sequence[UserOrm]:
    users = await UserRepository.get_users()
    return users


@user_router.get('/{id}')
async def get_user(id):
    user = await UserRepository.add_user(id)
    return user


@quiz_router.post('')
async def add_quiz(quiz: Quiz = Depends()) -> QuizId:
    id = await QuizRepository.add_quiz(quiz)
    return {"id": id}


@quiz_router.get('')
async def get_quizzes() -> list[QuizOrm]:
    quizzes = await QuizRepository.get_quizzes()
    return quizzes


@quiz_router.get('/{id}')
async def get_quiz(id):
    quiz = await QuizRepository.get_quiz(id)
    return quiz
