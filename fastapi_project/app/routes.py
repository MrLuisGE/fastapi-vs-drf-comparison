"""
API routes for Todo CRUD operations.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List

from . import models, schemas
from .database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: schemas.TodoCreate, session: Session = Depends(get_db)):
    """
    Create a new todo item.
    """
    db_todo = models.Todo(**todo.model_dump())
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/", response_model=List[schemas.TodoResponse])
async def list_todos(session: Session = Depends(get_db)):
    """
    Retrieve all todos.
    """
    todos = session.exec(select(models.Todo)).all()
    return todos


@router.get("/{todo_id}", response_model=schemas.TodoResponse)
async def get_todo(todo_id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific todo by ID.
    """
    todo = session.get(models.Todo, todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    return todo


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
async def update_todo(
    todo_id: int, 
    todo_update: schemas.TodoUpdate, 
    session: Session = Depends(get_db)
):
    """
    Update an existing todo.
    """
    db_todo = session.get(models.Todo, todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    
    # Update only provided fields
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_todo, field, value)
    
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, session: Session = Depends(get_db)):
    """
    Delete a todo by ID.
    """
    db_todo = session.get(models.Todo, todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id {todo_id} not found"
        )
    
    session.delete(db_todo)
    session.commit()
    return None
