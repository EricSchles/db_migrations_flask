from app import db

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    elem = db.Column(db.String)

    def __init__(self,elem):
        self.elem = elem

    def __repr__(self):
        return self.elem
