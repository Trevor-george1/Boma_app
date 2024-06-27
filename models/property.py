#!/usr/bin/python3
"""creates a property class that inherits from base model"""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Property(BaseModel, Base):
    """property class"""
    __tablename__ = "properties"
    property_name = Column(String(128), nullable=False)
    no_of_workers = Column(Integer(), nullable=False)
    no_of_houses = Column(Integer(), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
