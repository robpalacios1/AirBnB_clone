#!/usr/bin/env python
'''class inherent of BaseModel'''


class City(BaseModel):
    '''class city'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__

        self.stateid = ""
        self.name = ""
