#!/usr/bin/python3
"""
    Script that changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database "
              "state_name".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, db_name = sys.argv[1:4]

    # Create engine and connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query for the state
    state = session.query(State).filter(State.id == 2).first()

    # Print the result
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    # Close session
    session.close()
