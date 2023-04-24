import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False)
    username = Column(String(300), nullable=False)
    password = Column(String(300), nullable=False)
    biography = Column(String(400))

class Followers(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey("user.id"))
    to_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"))
    id_post = Column(Integer, ForeignKey("post.id"))
    message = Column(String(300), nullable=False)
    comment = relationship("User")
    post = relationship("Post")

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    link_media = Column(String(500), nullable=False)
    id_post = Column(Integer, ForeignKey("post.id"))
    post = relationship("Post")
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
