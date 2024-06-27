#!/usr/bin/python3
"""creates a Worker class that inherits from base model"""

from models.base_model import BaseModel


class Worker(BaseModel):
    """Worker class"""
    worker_id = ""
    worker_name = ""
    occupation = ""
    property_id = ""
    house_id = ""
