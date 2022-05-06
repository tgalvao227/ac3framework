# models.py


import datetime
from app import db


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    cat = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)

    def __init__(self, text, cat, price):
        self.text = text
        self.cat = cat
        self.price = price
        self.date_posted = datetime.datetime.now()
    

