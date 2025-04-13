from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, join

engine = create_engine("sqlite:///sqlalchemysample.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    
class Adress(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)
    
Base.metadata.create_all(engine)
Base.metadata.bind = engine

new_person = Person(name="Bill")
session.add(new_person)

session.commit()

new_address = Adress(post_code='0000', person=new_person)
session.add(new_address)
session.commit()

for person in session.query(Person).all():
    print(person.name)
    

results = session.query(Person, Adress).join(Adress).all()
for person, address in results:
    print(f"Person: {person.name}, Address: {address.post_code}")
    


