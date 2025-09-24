from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

db_url = "sqlite:///database.db"

Base = declarative_base()

engine = create_engine(db_url)

LocalSession = sessionmaker(bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()