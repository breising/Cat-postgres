from flask import Flask, redirect, render_template, url_for, request, flash, jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import User, Base, Category, Item
from flask import session as login_session


engine = create_engine(
    'postgresql://catalog:bcr0072@localhost:5432/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        # returns just the user.id value (integer)
        return user.id
    except:
        return None
