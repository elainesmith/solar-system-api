from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30))
    descr = db.Column(db.String)
    num_of_starbucks = db.Column(db.Integer)
