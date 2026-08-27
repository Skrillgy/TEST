import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.getenv('DATABASE_URL',
                         'postgresql+psycopg://navalbattle:navalbattle@localhost:5432/navalbattle')
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            aiutocommit=False)
class Base(DeclarativeBase):
    pass