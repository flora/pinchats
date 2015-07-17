from pinchats import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class User(Base):

    __tablename__ = "user"
    name = Column(String(120), nullable=False)
    email = Column(String(80), primary_key=True, nullable=False)
    frequency = Column(String(80), nullable=False)
    team = Column(String(80), nullable=False)
    role = Column(String(80), nullable=False)
    time_at_company = Column(String(120), nullable=False)
    last_scheduled = Column(DateTime, nullable=True)
    date_joined = Column(DateTime, nullable=False)
    active = Column(Boolean, nullable=False)

    def __init__(self, name, email, frequency, team, role, time_at_company, last_scheduled, date_joined, active):
        self.name = name
        self.email = email
        self.frequency = frequency
        self.team = team
        self.role = role
        self.time_at_company = time_at_company
        self.last_scheduled = last_scheduled
        self.date_joined = date_joined
        self.active = active

    def __repr__(self):
        return '<User %r>' % self.email
