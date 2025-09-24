from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from src.utils.db import get_db
from src.user_controller import *
from src.blog_controller import *
from src.dtos import UserSchema, LoginSchema, BlogSchema

userRouter = APIRouter(prefix="/user")
blogRouter = APIRouter(prefix="/blogs")

@userRouter.post("/register")
def register_user(body: UserSchema, db: Session = Depends(get_db)):
    return register(body, db)

@userRouter.post("/login")
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    return login(body, db)

@userRouter.get("/")
def my_profile(req: Request):
    user = req.state.user
    return fetchMyProfile(user)

@userRouter.put("/")
def update_user(req: Request, body: UserSchema, db: Session = Depends(get_db)):
    user = req.state.user
    return updateUser(body, db, user)

@userRouter.delete("/") 
def delete_user(req: Request, db: Session = Depends(get_db)):
    user = req.state.user
    return deleteUser(db, user)

@userRouter.post("/blog")
def create_blog(req: Request, body: BlogSchema, db: Session = Depends(get_db)):
    user = req.state.user
    return createBlog(body, db, user)

@userRouter.get("/blog") 
def get_blog(req: Request, db: Session = Depends(get_db)):
    user = req.state.user
    return getBlogs(db, user)

@userRouter.put("/blog")
def update_blog(req: Request, body: BlogSchema, db: Session = Depends(get_db)):
    user = req.state.user
    return updateBlog(req, body, db, user)

@userRouter.delete("/blog")
def delete_router(req: Request, db: Session = Depends(get_db)):
    user = req.state.user
    return deleteBlog(req, db, user)

@blogRouter.get("/")
def get_all_blogs(db: Session = Depends(get_db)):
    return getAllBlog(db)
