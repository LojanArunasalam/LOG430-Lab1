from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

db_url = 'postgresql+psycopg2://admin:admin@localhost:5432/postgres'
engine = create_engine(db_url)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    description = Column(String)


class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class LineSale(Base):
    __tablename__ = "line_sales" 

    id = Columm(Integer, primary_key=True)

# Will create the database + the tables associated with it
Base.metadata.create_all(engine)