from pinchats import db

class User(db.Model):

    __tablename__ = "user"

    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(80), primary_key=True, nullable=False)
    frequency = db.Column(db.String(80), nullable=False)
    team_name = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    months_at_company = db.Column(db.Integer, nullable=False)
    last_scheduled = db.Column(db.DateTime, nullable=True)
    date_joined = db.Column(db.DateTime, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, email, frequency, team_name, role, months_at_company, last_scheduled, date_joined, active):
        self.name = name
        self.email = email
        self.frequency = frequency
        self.team_name = team_name
        self.role = role
        self.months_at_company = months_at_company
        self.last_scheduled = last_scheduled
        self.date_joined = date_joined
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.email
