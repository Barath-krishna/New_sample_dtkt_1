from fastapi import FastAPI
from app.controller import movie_controller
from app.db import database

# Create FastAPI instance
app = FastAPI(title="Movie Recommendation API", version="1.0")

# Create DB tables if they don't exist
database.Base.metadata.create_all(bind=database.engine)

# Include the movie controller routes
app.include_router(movie_controller.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API"}