"""
Pydantic schemas for request/response validation.
"""
from typing import Optional
from pydantic import BaseModel


class TodoCreate(BaseModel):
    """Schema for creating a new Todo."""
    title: str
    description: str
    completed: bool = False


class TodoUpdate(BaseModel):
    """Schema for updating a Todo. All fields are optional."""
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    """Schema for Todo responses, includes ID."""
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        from_attributes = True
