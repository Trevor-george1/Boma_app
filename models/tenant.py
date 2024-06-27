#!/usr/bin/python3
"""creates a Tenant class that inherits from base model"""

from models.base_model import BaseModel


class Tenant(BaseModel):
    """Tenant class"""
    tenant_name = ""
    property_name = ""
    house_no = ""
