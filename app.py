from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(120))
    alias = db.Column(db.String(80), primary_key=True)
    frequency = db.Column(db.String(80))
    team_name = db.Column(db.String(80))
    role = db.Column(db.String(80))
    months_at_company = db.Column(db.Integer)
    last_scheduled = db.Column(db.Date)

    def __init__(self, name, alias, frequency, team_name, role, months_at_company, last_scheduled):
        self.name = name
        self.alias = alias
        self.frequency = frequency
        self.team_name = team_name
        self.role = role
        self.months_at_company = months_at_company
        self.last_scheduled = last_scheduled

    def __repr__(self):
        return '<User %r>' % self.alias

app = Flask(__name__)

@app.route('/user', methods=['PUT'])
def addUser():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
