"""
Database configuration for FastAPI Todo application.
Uses SQLModel with SQLite for simplicity.
"""
from sqlmodel import create_engine, Session, SQLModel

# SQLite database URL
DATABASE_URL = "sqlite:///./todos.db"

# Create engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=True
)


def create_db_and_tables():
    """
    Create database tables.
    """
    SQLModel.metadata.create_all(engine)


def get_db():
    """
    Dependency function to get database session.
    Yields a database session and ensures it's closed after use.
    """
    with Session(engine) as session:
        yield session
