from system import db

class Category(db.Model):
    id = db.Column(db.Integer,primary_key = True,nullable=False)
    category = db.Column(db.String,nullable=False)