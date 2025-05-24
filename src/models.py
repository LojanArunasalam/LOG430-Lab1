from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

db_url = 'postgresql+psycopg2://admin:admin@localhost:5432/postgres'
engine = create_engine(db_url)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

# Will create the database + the tables associated with it
Base.metadata.create_all(engine)