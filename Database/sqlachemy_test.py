'''
CREATING SESSION
'''

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')
Session = sessionmaker(bind=engine)

# this loads the sqlalchemy base class
Base = declarative_base()

# this instantiates the session object
session = Session()

'''
INSERTING DATA
'''


# Setting up classes (creates the record objects and defines the schema)

class Customer(Base):
    __tablename__ = 'customer'
    # Here we define columns for the table customer
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    town = Column(String(250), nullable=False)


class Item(Base):
    __tablename__ = 'item'
    # Here we define columns for the table item
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cost_price = Column(Integer)
    selling_price = Column(Integer)
    quantity = Column(Integer)


class Order(Base):
    __tablename__ = 'order'
    # Here we define columns for the table order
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    customer = relationship("Customer", backref='order')

    # order_lines = Column(Integer,


class OrderLine(Base):
    __tablename__ = 'order_line'
    # Here we define columns for the table orderline
    id = Column(Integer, primary_key=True)
    order = Column(Integer, ForeignKey('order.id'))

    order_id = relationship("Order", backref="order_line")

    item = Column(Integer, ForeignKey('item.id'))

    item_id = relationship("Item", backref="order_line")

    quantity = Column(Integer)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden')

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )
c1, c2

# c1.first_name, c1.last_name
# c2.first_name, c2.last_name

# add the information from c1 and c2 to the Customer table
session.add(c1)
session.add(c2)

c1.id, c2.id

# commit the changes made (the added c1 and c2)
session.commit()

c3 = Customer(
    first_name="John",
    last_name="Lara",
    username="johnlara",
    email="johnlara@mail.com",
    address="3073 Derek Drive",
    town="Norfolk"
)

c4 = Customer(
    first_name="Sarah",
    last_name="Tomlin",
    username="sarahtomlin",
    email="sarahtomlin@mail.com",
    address="3572 Poplar Avenue",
    town="Norfolk"
)

c5 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c6 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

session.add_all([c3, c4, c5, c6])
session.commit()

i1 = Item(name='Chair', cost_price=9.21, selling_price=10.81, quantity=5)
i2 = Item(name='Pen', cost_price=3.45, selling_price=4.51, quantity=3)
i3 = Item(name='Headphone', cost_price=15.52, selling_price=16.81, quantity=50)
i4 = Item(name='Travel Bag', cost_price=20.1, selling_price=24.21, quantity=50)
i5 = Item(name='Keyboard', cost_price=20.1, selling_price=22.11, quantity=50)
i6 = Item(name='Monitor', cost_price=200.14, selling_price=212.89, quantity=50)
i7 = Item(name='Watch', cost_price=100.58, selling_price=104.41, quantity=50)
i8 = Item(name='Water Bottle', cost_price=20.89, selling_price=25, quantity=50)

session.add_all([i1, i2, i3, i4, i5, i6, i7, i8])
session.commit()

o1 = Order(customer=c1)
o2 = Order(customer=c1)

line_item1 = OrderLine(order=o1, item=i1, quantity=3)
line_item2 = OrderLine(order=o1, item=i2, quantity=2)
line_item3 = OrderLine(order=o2, item=i1, quantity=1)
line_item3 = OrderLine(order=o2, item=i2, quantity=4)

session.add_all([o1, o2])

session.new
session.commit()

o3 = Order(customer=c1)

orderline1 = OrderLine(item=i1, quantity=5)
orderline2 = OrderLine(item=i2, quantity=10)

# o3.order_lines.append(orderline1)
# o3.order_lines.append(orderline2)

session.add_all([o3])

session.commit()

'''
QUERYING DATA
'''
# ALL METHOD
session.query(Customer).all()

print(session.query(Customer))

q = session.query(Customer)

for c in q:
    print(c.id, c.first_name)

session.query(Customer.id, Customer.first_name).all()
