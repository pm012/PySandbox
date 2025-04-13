from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

users = Table('users', metadata, 
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
              )

addresses = Table('addresses', metadata, 
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False),
                  )

metadata.create_all(engine)

with engine.connect() as conn:
    ins1 = users.insert().values(name = "Jack Jones")
    print(str(ins1))
    conn.execute(ins1)
    
    ins2 = users.insert().values(name = "Serhii Crumb")
    conn.execute(ins2)    
    print(str(ins2))
    
    
    s = select(users)
    result = conn.execute(s)
    for row in result:
        print(row)




