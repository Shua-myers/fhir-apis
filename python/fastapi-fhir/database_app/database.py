from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: get from .env file instead
SQLALCHEMY_DATABASE_URL = "sqlite:///./database_app.db"

# reuseable engine for later on.  "check same thread" only needed for sqlite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# create SessionLocal class, each session will be an instance of this class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, binid=engine)

# Base class created to be inherited by other models later
Base = declarative_base()
