# Blog Management API

This component provides backend APIs for managing user blogs including creation, retrieval, updating, and deletion. Built using FastAPI, SQLAlchemy, and Pydantic.

Features
Create new blog posts linked to authenticated users

Get list of blogs by user or all blogs

Update blogs with authorization checks ensuring users can only update their own posts

Delete blogs with user ownership verification

JWT authentication for protecting routes

Easy integration with user management system

Setup and Installation
Clone the repository.

Setup a Python virtual environment and activate it.

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install fastapi sqlalchemy uvicorn pydantic passlib PyJWT
Configure environment variables such as SECRET_KEY for JWT and database credentials.

Run database migrations or use SQLAlchemy Base metadata for table creation.

Start your server:

bash
uvicorn src.main:app --reload
API Endpoints
POST /user/blog - Create blog post

GET /user/blog - Get all blogs of authenticated user

PUT /user/blog?id=<blog_id> - Update blog post by id

DELETE /user/blog?id=<blog_id> - Delete blog post by id

GET /blogs/ - Get all blogs (public)

Authentication
All /user/blog routes require JWT in the header under Authorization: Bearer <token>.

Project Structure
src/blog_controller.py - Blog CRUD logic

src/dtos.py - BlogSchema

src/models.py - SQLAlchemy Blog model

src/user_controller.py - User related logic and authentication

src/user_routes.py - API routing for users and blogs

src/middlewares/auth_middleware.py - Middleware for token authentication

Contributing
Feel free to submit issues or pull requests for enhancements or bugs.