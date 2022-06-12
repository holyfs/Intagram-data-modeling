import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followers_id=Column(Integer, ForeignKey('followers.id'))

class Followers(Base):
    __tablename__ = 'followers'
    followers_id=Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(250), nullable=False)
    followers_id=(Integer, ForeignKey('followers.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    favorites_id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    followers_id=Column(Integer, ForeignKey('followers.id'))

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e