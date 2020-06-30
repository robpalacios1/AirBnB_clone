#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''class amenity'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''initialize Amenity'''
        if kwargs:
            super().__init__(*args, **kwargs)
