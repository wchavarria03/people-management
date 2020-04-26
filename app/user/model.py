from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    birthday = db.Column(db.String())
    created_at = db.Column(db.String())

    def __init__(self, first_name, last_name, birthday, created_at):
        self.first_name = first_name
        self.Last_name = last_name
        self.birthday = birthday
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'fist_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'created_at':self.created_at
        }
