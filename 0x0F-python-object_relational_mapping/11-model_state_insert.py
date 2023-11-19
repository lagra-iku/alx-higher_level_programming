#!/usr/bin/python3
"""
a script that inserts State objects into the
database hbtn_0e_6_usa using SQLAlchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    result = session.query(State).filter(State.name == 'Louisiana')
    for row in result:
        print(row.id)
    session.close()
