#!/usr/bin/python3
"""creates a House class that inherits from base model"""

from models.base_model import BaseModel

class House(BaseModel):
    """House class"""
    property_id = ""
    tenant_name = ""
    property_name = ""
    house_no = ""
    price = ""
    status = ""
