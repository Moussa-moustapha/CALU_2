#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship

class Event(BaseModel, Base):
    __tablename__ = 'events'
    name = Column(String(128), nullable=False, unique=True)
    club_id = Column(String(60), ForeignKey('clubs.id'), nullable=True)
    description = Column(String(128), nullable=True)
    location = Column(String(128), nullable=True)
    date = Column(String(128), nullable=True)
    time = Column(String(128), nullable=True)