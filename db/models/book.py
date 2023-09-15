from sqlalchemy import Column, Integer, String
from db.config import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, )
    author = Column(String(50), nullable=False)
    release_year = Column(Integer, nullable=False)

    