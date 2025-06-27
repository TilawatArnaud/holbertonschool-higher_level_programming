#!/usr/bin/python3
"""
    Script that lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query and print first State object
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    
    # Close session
    session.close()