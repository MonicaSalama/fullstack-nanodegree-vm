from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
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


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
User1.hash_password('12345')
session.add(User1)
session.commit()

# Menu for UrbanBurger
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Two shinguards", description="Two shinguards description",
                     category=category1)

session.add(item1)
session.commit()


item2 = Item(user_id=1, name="Shinguards", description="Shinguards description",
                     category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Jersey", description="Jersey description",
                     category=category1)

session.add(item3)
session.commit()


item4 = Item(user_id=1, name="Soccer Cleats", description="Soccer Cleats description",
                     category=category1)

session.add(item4)
session.commit()


# Menu for Super Stir Fry
category2 = Category(user_id=1, name="Basketball")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="BasketBall item", description="BasketBall item description",
                     category=category2)

session.add(item1)
session.commit()


# Items for Baseball
category1 = Category(user_id=1, name="Baseball")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Bat", description="Bat item description",
                     category=category1)

session.add(item1)
session.commit()


# Menu for Thyme for that
category1 = Category(user_id=1, name="Frisbee")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Frisbee item", description="Frisbee item description",
                     category=category1)

session.add(item1)
session.commit()


# Items for Snowboarding
category1 = Category(user_id=1, name="Snowboarding")

session.add(category1)
session.commit()


item1 = Item(user_id=1, name="Goggles", description="Goggles description",
                     category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Snowboard", description="Snowboard description",
                     category=category1)

session.add(item2)
session.commit()


# Items for Rock Climbing
category1 = Category(user_id=1, name="Rock Climbing")

session.add(category1)
session.commit()



# Items for Foosball
category1 = Category(user_id=1, name="Foosball")

session.add(category1)
session.commit()


# Items for Skating
category1 = Category(user_id=1, name="Skating")

session.add(category1)
session.commit()


category1 = Category(user_id=1, name="Hockey")
session.add(category1)
session.commit()

print "added category items!"
