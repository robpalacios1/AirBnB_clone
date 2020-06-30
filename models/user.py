#!/usr/bin/env python
'''A class user that inherent from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''represent a class User'''

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
