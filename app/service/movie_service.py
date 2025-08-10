from sqlalchemy.orm import Session
from app.models import models


# =========================
# User Services
# =========================
def create_user(db: Session, username: str, email: str):
    new_user = models.User(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(models.User).all()


# =========================
# Movie Services
# =========================
def create_movie(db: Session, movie_name: str, director: str, genre: str, description: str, release_year: int):
    new_movie = models.Movie(
        movie_name=movie_name,
        director=director,
        movie_genre=genre,
        description=description,
        release_year=release_year
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie


def get_movies(db: Session):
    return db.query(models.Movie).all()


# =========================
# Rating Services
# =========================
def create_rating(db: Session, user_id: int, movie_id: int, rating: int, review: str):
    new_rating = models.Rating(
        user_id=user_id,
        movie_id=movie_id,
        rating=rating,
        review=review
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating


def get_ratings(db: Session):
    return db.query(models.Rating).all()