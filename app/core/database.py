from sqlmodel import create_engine, Session
from app.models import *
import os
from dotenv import load_dotenv

load_dotenv()

postgres_url = os.getenv("POSTGRES_URL")

engine = create_engine(postgres_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

print(engine.url)