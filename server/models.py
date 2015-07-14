from pinchats import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class User(Base):

    __tablename__ = "user"
    name = Column(String(120), nullable=False)
    email = Column(String(80), primary_key=True, nullable=False)
    frequency = Column(String(80), nullable=False)
    team_name = Column(String(80), nullable=False)
    role = Column(String(80), nullable=False)
    months_at_company = Column(Integer, nullable=False)
    last_scheduled = Column(DateTime, nullable=True)
    date_joined = Column(DateTime, nullable=False)
    active = Column(Boolean, nullable=False)

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
