#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship

class Club(BaseModel, Base):
    __tablename__ = 'clubs'
    name = Column(String(128), nullable=True, unique=True)
    owner_id = Column(String(128), ForeignKey('users.id'), nullable=True)
    events = relationship('Event', backref='clubs')
    # members = relationship('User', backref='clubs')
    discripton = Column(String(128), nullable=True)
    member_count = Column(Integer, nullable=True)
    attraction_count = Column(Integer, nullable=True)


    def __init__(self, *args, **kwargs):
        """Initializes User object with super class constructor"""
        super().__init__(*args, **kwargs)