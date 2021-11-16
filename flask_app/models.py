from database import db

class Note(db.Model):
    if = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", dbString(200))
    text = db.Column("text", db.String(100))
    date = db.Column("date", db.String(50))

    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date
class User(db.Model):
    id = db.Columnm("id", db.Integer, primary_key=True)
    name = db.column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email
