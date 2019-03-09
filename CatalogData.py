from databaseSetup import Base, Category, Item, User
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


engine = create_engine
('sqlite:///CatalogApplication.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="BasketBall")
session.add(category1)
session.commit()

category2 = Category(name="Soccer")
session.add(category2)
session.commit()

category3 = Category(name="Baseball")
session.add(category3)
session.commit()

category4 = Category(name="Frisbee")
session.add(category4)
session.commit()

category5 = Category(name="Snowboarding")
session.add(category5)
session.commit()

category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="Skating")
session.add(category7)
session.commit()


User1 = User(name="System", email="shreya957@gmail.com")
session.add(User1)
session.commit()

ItemC1 = Item(name="Breakaway rim",
              description="A breakaway rim is a \
              basketball rim that contains a hinge \
              and a spring at the point",
              cat_id=Category1.id, user_id=User1.id)
session.add(ItemC1)
session.commit()

ItemC2 = Item(name="Shin Guard",
              description="A shin guard or shin pan is \
              a piece of equipment worn on the front of a \
              players shin to protect them  from injury",
              cat_id=Category2.id, user_id=User1.id)
session.add(ItemC2)
session.commit()

ItemC3 = Item(name="Soccer Ball", description="A football, soccer \
 ball, or association football ball is the ball used in the sport of \
 association football.", cat_id=Category2.id, user_id=User1.id)
session.add(ItemC3)
session.commit()

ItemC4 = Item(name="Baseball Gloves",
              description="A baseball glove or mitt is a large leather \
              glove worn by baseball players of the defending team",
              cat_id=Category3.id, user_id=User1.id)
session.add(ItemC4)
session.commit()

ItemC5 = Item(name="Flying Discs",
              description="It is used recreationally and competitively for \
              throwing and catching", cat_id=Category4.id, user_id=User1.id)
session.add(ItemC5)
session.commit()

ItemC6 = Item(name="Snowboard", description="Snowboards are boards where \
both feet are secured to the same board, which are wider than skis,\
 with the ability to glide on snow", cat_id=Category5.id, user_id=User1.id)
session.add(ItemC6)
session.commit()

ItemC7 = Item(name="Snowboarding Boots",
              description="The boots used in snowboarding are generally soft \
              plastic boots except in case of alpine snowboarding",
              cat_id=Category5.id, user_id=User1.id)
session.add(ItemC7)
session.commit()

ItemC8 = Item(name="Snowboarding Boots",
              description="The boots used in snowboarding are generally soft \
              plastic bootscase of alpine snowboarding",
              cat_id=Category5.id, user_id=User1.id)
session.add(ItemC8)
session.commit()

ItemC9 = Item(name="Climbing Harnesses", description=" A harness secures \
a person to a rope or an anchor point.", cat_id=Category6.id, user_id=User1.id)
session.add(ItemC9)
session.commit()

ItemC10 = Item(name="Climbing Rope",
               description="A dynamic rope is a specially constructed, \
               somewhat elastic rope used primarily in rock climbing.",
               cat_id=Category6.id, user_id=User1.id)
session.add(ItemC10)
session.commit()

ItemC11 = Item(name="Skates", description="Basic skates for Ice Skating",
               cat_id=Category7.id, user_id=User1.id)
session.add(ItemC11)
session.commit()

print "added category items!"
