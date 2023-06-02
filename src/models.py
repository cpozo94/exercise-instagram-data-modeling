import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,  primary_key=True, nullable=False)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False) 
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), primary_key=True, nullable=False)
    password = Column(String(100), nullable=False)
    followers = relationship('Follower')

class Post(Base):
    __tablename__ = 'post'
    id = Column (Integer,  primary_key=True, nullable=False)
    post_date = Column (Date, nullable=False)
    image = Column (String(250), nullable=False)
    description = Column(Text())
    user_id= Column(String, ForeignKey('user.id'))
    user=relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column (Integer,  primary_key=True, nullable=False)
    comment_text = Column (Text(), nullable=False)
    comment_date = Column (Date, nullable=False)
    post_id = Column(String, ForeignKey('post.id'))
    follower_id = Column(String, ForeignKey('follower.id'))
    post= relationship('Post')
    follower= relationship('Follower')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

    



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
