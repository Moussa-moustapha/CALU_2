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
    

    def __init__(self, *args, **kwargs):
        """Initializes User object with super class constructor"""
        super().__init__(*args, **kwargs)