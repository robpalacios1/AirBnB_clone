#!/Usr/Bin/python3
'''module 'base_model'''


import uuid
from datetime import datetime

import models


class BaseModel():
    '''class BaseModel'''
    def __init__(self, *args, **kwargs):
        '''class constructor for class BaseModel'''
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''string of BaseModel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''updates 'updated_at' instance with current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''dictionary representation of instance'''
        new_dict = dict(self._dict_)
        new_dict['created_at'] = self._dict_['created_at'].isoformat()
        new_dict['updated_at'] = self._dict_['updated_at'].isoformat()
        new_dict['_class'] = self.class.name_
        return (new_dict)
