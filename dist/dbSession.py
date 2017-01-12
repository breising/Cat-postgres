from flask import Flask
#, redirect, render_template, request, flash
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import User, Base, Category, Item
#from flask import session as login_session

app = Flask(__name__)


# Original code works with sqlite

# below, identify the db that you want to work with...
# engine = create_engine('sqlite:///catalog.db')
# # associate your engine with the session
# Session = sessionmaker(bind=engine)
# # create an instance of the Session to use in your code
# session = Session()


# New code to connect to Postgres DB

# below, identify the db that you want to work with...
engine = create_engine(
    'postgresql://postgres:bcr0072@localhost:5432/postgres')
# associate your engine with the session
Session = sessionmaker(bind=engine)
# create an instance of the Session to use in your code
session = Session()
