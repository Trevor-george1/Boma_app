#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.house import House

all_objs = storage.all()
print("-- Reload objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new House --")
my_house = House()
my_house.property_id = "006"
my_house.tenant_name = "Larry Kennedy"
my_house.property_name = "Joksa Properties"
my_house.house_no = "001"
my_house.price = "12,000"
my_house.status = "single room"
my_house.save()
print(my_house)
