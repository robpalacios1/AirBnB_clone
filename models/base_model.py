#!/usr/bin/python3
'''module 'base_model'''


import uuid
from datetime import datetime

import models


class BaseModel():
    '''class BaseModel'''
    def __init__(self, id=None):
        '''class constructor for class BaseModel'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        '''string of BaseModel instance'''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        '''updates 'updated_at' instance with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''dictionary representation of instance'''
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return (new_dict)
