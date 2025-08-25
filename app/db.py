from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# For SQLite, check_same_thread must be False for multithreaded ASGI servers
engine = create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
	"""Dependency that provides a SQLAlchemy session and ensures cleanup."""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

