from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from fastapi_utils.guid_type import setup_guids_postgresql

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/python_fast_api_core_app"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def dbs():
#     session = SessionLocal()
#     try:
#         yield session
#     finally:
#         session.close()

Base = declarative_base()
db = Session(engine, future=True)