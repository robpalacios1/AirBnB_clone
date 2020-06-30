#!/usr/bin/python3
'''class inherent of BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''class State'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''initialize State'''
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__
