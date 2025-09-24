# Blog Management API

This component provides backend APIs for managing user blogs including creation, retrieval, updating, and deletion. Built using FastAPI, SQLAlchemy, and Pydantic.

## Features

- Create new blog posts linked to authenticated users  
- Get list of blogs by user or all blogs  
- Update blogs with authorization checks ensuring users can only update their own posts  
- Delete blogs with user ownership verification  
- JWT authentication for protecting routes  
- Easy integration with user management system  

## Setup and Installation

1. Clone the repository.

2. Setup a Python virtual environment and activate it:

python -m venv env
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. Install dependencies:

pip install fastapi sqlalchemy uvicorn pydantic passlib PyJWT

4. Configure environment variables such as `SECRET_KEY` for JWT and database credentials.

5. Run database migrations or use SQLAlchemy Base metadata for table creation.

6. Start the server:

fastapi dev main.py

## API Endpoints

- `POST /user/blog` - Create blog post  
- `GET /user/blog` - Get all blogs of authenticated user  
- `PUT /user/blog?id=<blog_id>` - Update blog post by id  
- `DELETE /user/blog?id=<blog_id>` - Delete blog post by id  
- `GET /blogs/` - Get all blogs (public)  

## Authentication

All `/user/blog` routes require JWT token in the header:

Authorization: Bearer <token>

## Project Structure

- `src/blog_controller.py` - Blog CRUD logic  
- `src/dtos.py` - BlogSchema  
- `src/models.py` - SQLAlchemy Blog model  
- `src/user_controller.py` - User-related logic and authentication  
- `src/user_routes.py` - API routing for users and blogs  
- `src/utils/auth_middleware.py` - Middleware for token authentication  

## Contributing

Feel free to submit issues or pull requests for enhancements or bug fixes.
