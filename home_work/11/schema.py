from pydantic import BaseModel, ConfigDict


class UserId(BaseModel):
    id: int


class UserAdd(BaseModel):
    name: str
    age: int
    phone: int | None = None


class User(UserAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class QuizId(BaseModel):
    id: int


class Quiz(QuizId):
    name: str
    user_id: int
    model_config = ConfigDict(from_attributes=True)


class QuestionId(BaseModel):
    id: int


class QuestionAdd(QuestionId):
    question: str
    answer: str
    wrong1: str
    wrong2: str
    wrong3: str
    model_config = ConfigDict(from_attributes=True)