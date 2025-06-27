#!/usr/bin/python3
"""
Module that defines the State class and an instance Base = declarative_base()
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of declarative_base
Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States
        id (sqlalchemy.Integer): The state's id
        name (sqlalchemy.String): The state's name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Create engine that stores data in the local directory's
    # hbtn_0e_6_usa database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],  # MySQL username
        sys.argv[2],  # MySQL password
        sys.argv[3]   # Database name
    ), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()

    # Query all State objects and print them
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
