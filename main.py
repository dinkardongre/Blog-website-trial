from fastapi import FastAPI
from src.utils.db import Base, engine
from src.router import userRouter, blogRouter
from src.utils.helper import Authmiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(Authmiddleware)

app.include_router(userRouter)
app.include_router(blogRouter)

@app.get("/")
def welcome():
    return {"message": "Code is running fine..."}
