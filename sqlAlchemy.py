from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Pizza(Base):
    def __init__(self, name, crust, sauce, cheese, toppings):    
        self.name = name
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
        
    __tablename__ = 'pizza'
    
    id = Column( Integer, primary_key = True )
    name = Column( String )                       
    crust = Column( String )
    sauce = Column( String )
    cheese = Column( String )
    toppings = Column( String )
    
    def __repr__(self):
        return "<pizza(name={0}, crust={1}, sauce={2}, cheese={3}, toppings={4})>".format(self.name, self.crust, self.sauce, self.cheese, self.toppings)
    
def main():
    engine = create_engine('sqlite:///:memory:', echo = False)
    
    Base.metadata.create_all(engine)
    
    pizza1 = Pizza("Pepporoni", "White Flour", "Tomato", "Mozzeralla/Provel Blend", "Pepporoni")
    print (pizza1)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.add(pizza1)
    
    newPizza1 = session.query(Pizza).filter_by(name = "Pepporoni").first()
    
    pizza1.cheese = 'Mozzeralla'
    print(session.dirty)
    session.commit()
    
    print(pizza1.id)
    
    session.add_all([
        Pizza(name = "Cheese", crust = "White Flour", sauce = "Tomato", cheese = "Mozzeralla/Provel Blend", toppings = "None"),
        Pizza(name = "Deluxe", crust = "White Flour", sauce = "Tomato", cheese = "Mozzeralla/Provel Blend", toppings = "Pepporoni, Mushroom, Purple Onion, Olive, Peppered Bacon, Green Pepper"),])
    session.commit()
    
    for row in session.query(Pizza).all():
        print(row.name, row.toppings)
        
main()
