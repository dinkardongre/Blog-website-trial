from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hash_password = Column(String, nullable=False)

    blogs = relationship("Blog", back_populates="users", passive_deletes="all, delete-orphan")

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    header_image = Column(String, nullable=False)

    users = relationship("User", back_populates="blogs", passive_deletes=True)
    