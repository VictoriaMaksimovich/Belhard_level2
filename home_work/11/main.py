import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from schema import UserId

app = FastAPI()


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