from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import Request
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from sqlalchemy.orm import Session
from src.user_controller import SECRET_KEY, ALGORITHM, get_user_by_username
from src.utils.db import get_db

class Authmiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request : Request, call_next):
        public_paths = ["/user/login", "/user/register", "/blogs"]

        if any(request.url.path.startswith(path) for path in public_paths):
            return await call_next(request)
        
        token = request.headers.get("authorization")
        if not token or not token.startswith("Bearer "):
            return JSONResponse(status_code=401, content={
                "Error":"You are not authorized"
            })
        token = token.split(" ")[1]

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except ExpiredSignatureError:
            return JSONResponse(status_code=401, content={"Error":"Token has expired"})
        except InvalidTokenError:
            return JSONResponse(status_code=401, content={"Error":"Invalid token"})
        
        username = data.get("username")
        if not username:
            return JSONResponse(status_code=401, content={"Error":"You are not authorized"})
        db = next(get_db())
        user = get_user_by_username(username, db)

        if not user:
            return JSONResponse(status_code=401, content={"Error":"You are not authorized"})
        
        request.state.user = user

        response = await call_next(request)
        return response