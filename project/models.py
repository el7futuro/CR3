from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)

class Director(models.Base):
    __tablename__ = 'director'

    name = Column(String(100), unique=True, nullable=False)

class Movie(models.Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    description = Column(String(255))
    trailer = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")
    director_id = Column(Integer, ForeignKey("director.id"))
    director = relationship("Director")