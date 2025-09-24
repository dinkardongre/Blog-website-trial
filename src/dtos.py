from pydantic import BaseModel

class UserSchema(BaseModel):
    name : str
    email : str
    username : str
    password : str

class LoginSchema(BaseModel):
    username : str
    password : str

class BlogSchema(BaseModel):
    title : str
    content : str
    header_image : str