from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service import movie_service


router = APIRouter()


# =========================
# User Endpoints
# =========================
@router.post("/users")
def create_user(username: str, email: str, db: Session = Depends(get_db)):
    return movie_service.create_user(db, username, email)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return movie_service.get_users(db)


# =========================
# Movie Endpoints
# =========================
@router.post("/movies")
def create_movie(movie_name: str, director: str, genre: str, description: str, release_year: int, db: Session = Depends(get_db)):
    return movie_service.create_movie(db, movie_name, director, genre, description, release_year)


@router.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return movie_service.get_movies(db)


# =========================
# Rating Endpoints
# =========================
@router.post("/ratings")
def create_rating(user_id: int, movie_id: int, rating: int, review: str, db: Session = Depends(get_db)):
    return movie_service.create_rating(db, user_id, movie_id, rating, review)


@router.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return movie_service.get_ratings(db)
