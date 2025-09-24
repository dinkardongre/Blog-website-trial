from fastapi import HTTPException, Request, status
from sqlalchemy.orm import Session
from src.dtos import BlogSchema
from src.models import Blog, User

def createBlog(body: BlogSchema, db: Session, user: User):
    if not user:
        raise HTTPException(401, detail={"Error": "Access denied/unauthorized access..."})
    newBlog = Blog(**body.model_dump(), user_id=user.id)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)

    return {
        "Status": f"New blog created by {user.name}",
        "New-Blog": newBlog
    }

def getAllBlog(db: Session):
    return db.query(Blog).all()

def getBlogs(db: Session, user: User):
    if not user:
        raise HTTPException(401, detail={"Error": "Access denied/unauthorized access..."})
    blogs = db.query(Blog).filter(Blog.user_id == user.id).all()
    if not blogs:
        return f"{user.name} has no blogs."
    return blogs

def updateBlog(req: Request, body: BlogSchema, db: Session, user: User):
    if not user:
        raise HTTPException(401, detail={"Error": "Access denied/unauthorized access..."})
    blog_id = req.query_params.get("id")
    if not blog_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Blog ID is required")
    blog = db.query(Blog).filter(Blog.id == int(blog_id)).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Blog not found")
    if blog.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not authorized to update this blog")
    data = body.model_dump()
    for k, v in data.items():
        setattr(blog, k, v)
    db.commit()
    db.refresh(blog)

    return {
        "Status": f"Blog updated successfully by {user.name}",
        "updated-blog": blog
    }

def deleteBlog(req: Request, db: Session, user: User):
    if not user:
        raise HTTPException(401, detail={"Error": "Access denied/unauthorized access..."})
    blog_id = req.query_params.get("id")
    if not blog_id:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Blog ID is required")
    blog = db.query(Blog).filter(Blog.id == int(blog_id)).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Blog not found")
    if blog.user_id != user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not authorized to delete this blog")
    db.delete(blog)
    db.commit()

    return {
        "Status": f"Blog deleted by {user.name}",
        "deleted-blog": blog
    }
