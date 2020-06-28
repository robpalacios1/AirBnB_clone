#!/Usr/Bin/python3
'''module 'base_model'''


import uuid
from datetime import datetime

import models


class BaseModel():
    '''class BaseModel'''
    def _init_(self, *args, **kwargs):
        '''class constructor for class BaseModel'''
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '_class_':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def _str_(self):
        '''string of BaseModel instance'''
        return "[{}] ({}) {}".format(self._class.name_,
                                     self.id, self._dict_)

    def save(self):
        '''updates 'updated_at' instance with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''dictionary representation of instance'''
        new_dict = dict(self._dict_)
        new_dict['created_at'] = self._dict_['created_at'].isoformat()
        new_dict['updated_at'] = self._dict_['updated_at'].isoformat()
        new_dict['_class'] = self.class.name_
        return (new_dict)
