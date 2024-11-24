from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from database import create_tables, add_test_data, delete_tables
from router import user_router, quiz_router
from schema import UserId


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await add_test_data()
    print("------Bases build-------------")
    yield
    await delete_tables()
    print("-------------Bases droped------------")


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(quiz_router)


class STaskAdd(BaseModel):
    name: str
    description: str | None = None


@app.get('/', tags='Hello')
async def home():
    return {"name": "Name1"}


@app.post('/')
async def add_task(task: STaskAdd = Depends()):
    return {"data": task}


# @app.get('/user/{id}', response_model=UserId)
# async def get_user_info(id: int, ):



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
