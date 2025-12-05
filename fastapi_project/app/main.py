"""
FastAPI Todo Application - Main entry point.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from .database import create_db_and_tables
from .routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler to create database tables on startup.
    """
    create_db_and_tables()
    yield

app = FastAPI(
    title="FastAPI Todo API",
    description="A simple Todo API built with FastAPI for comparison with Django REST Framework",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint - API health check.
    """
    return {
        "message": "Welcome to FastAPI Todo API",
        "docs": "/docs",
        "redoc": "/redoc",
        "version": "1.0.0"
    }


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
