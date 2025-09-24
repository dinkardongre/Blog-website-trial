import jwt as pyjwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from src.dtos import UserSchema, LoginSchema
from src.models import User

SECRET_KEY = "29fda3b6bb9548ffada7be82af6a76598ef0bd31f348cf7f2bbbd1d4bfceed0f"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_by_username(username:str,database:Session):
    user = database.query(User).filter(User.username == username).first()
    if not user:
        return None
    return user

def register(body:UserSchema, database:Session):
    currentUser = get_user_by_username(body.username, database)
    if currentUser:
        raise HTTPException(409, detail={"Error":"User already exist"})
    
    hp = get_password_hash(body.password)

    user = User(
        name=body.name,
        email=body.email,
        username=body.username,
        hash_password=hp
    )

    database.add(user)
    database.commit()
    database.refresh(user)

    return {
        "status":"User created successfully...",
        "user":user
    }

def login(body:LoginSchema, database:Session):
    currentUser = get_user_by_username(body.username, database)
    if not currentUser:
        raise HTTPException(404, detail={"Error":"User not found"})

    verifyPassword = verify_password(body.password, currentUser.hash_password)

    if not verifyPassword:
        raise HTTPException(404, detail="Password is incorrect")

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = pyjwt.encode({"username":currentUser.username, "exp":expire}, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "Message":"Login Successfully....",
        "token":token
    }

def fetchMyProfile(user:User):
    if not user:
        raise HTTPException(401, detail={"Error":"Access denied/unauthorized access..."})
    return {
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "username": user.username,
        },
        "blogs":user.blogs
    }

def updateUser(body:UserSchema, db:Session, user:User):
    if not user:
        raise HTTPException(401, detail={"Error":"Access denied/unauthorized access..."})
    user_db = db.query(User).filter(User.id == user.id).first()
    if not user_db:
        raise HTTPException(404, detail={"Error": "User not found"})
    data = body.model_dump()
    for k, v in data.items():
        setattr(user_db, k, v)
    db.commit()
    db.refresh(user_db)
    return {"Status": "User updated successfully", "UpdatedUser": user_db}

def deleteUser(db: Session, user:User):
    if not user:
        raise HTTPException(401, detail={"Error":"Access denied/unauthorized access..."})
    user_db = db.query(User).filter(User.id == user.id).first()
    if not user_db:
        raise HTTPException(404, detail={"Error": "User not found"})
    db.delete(user_db)
    db.commit()
    return {"Message": "User deleted", "DeletedUser": user_db}
