#!/usr/bin/python3
'''A class FileStorage that serializes instances to JSON file'''

from models.base_model import BaseModel
from models.user import User
import json


class FileStorage:
    '''Represents a class FileStorage'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''Returns a dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in objects'''
        type(self).__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        '''Serializes __objects to the JSON file'''
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w",
                  encoding='utf-8')as write_file:
            json.dump(new_dict, write_file)

    def reload(self):
        '''Deserializes the JSON file to __objects'''
        try:
            with open(FileStorage.__file_path, "r",
                      encoding='utf-8') as read_file:
                type(self).__objects = json.load(read_file)
            for key, value in type(self).__objects.items():
                obj = eval(type(self).__objects[key]['__class__'])(**value)
                type(self).__objects[key] = obj

        except FileNotFoundError:
            pass
