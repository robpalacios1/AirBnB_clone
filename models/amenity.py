#!/usr/bin/env python
'''class inherent of BaseModel'''


class Amenity(BaseModel):
    '''class amenity'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__

        self.name = ""
