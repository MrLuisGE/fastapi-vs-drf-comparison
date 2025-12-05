"""
SQLModel models for the Todo application.
"""
from typing import Optional
from sqlmodel import Field, SQLModel


class Todo(SQLModel, table=True):
    """
    Todo model representing a task item.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool = False
