#!/usr/bin/python3
'''Method Command Interpreter'''
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}

    def do_create(self, args):
        '''Create a new instance of BaseModel, save it and prints the id
           Usage: create <class name>
        '''
        if not args:
            print("** class name missing **")
        else:
            if args in HBNBCommand.classes:
                new_creation = eval(args + '()')
                models.storage.save()
                print(new_creation.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        '''Prints the string representation of a specific instance
           Usage: show <class name> <id>
        '''
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = strings[0] + '.' + strings[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        '''Delete an instance
           Usage: destroy <class name> <id>
        '''
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                del models.storage.all()[key_value]
                models.storage.save()
            except KeyError:
                print(" ** no instance found **")

    def do_all(self, args):
        '''Print a string representation of all instances
           Usage: all <class name>
        '''
        strings = args.split()
        new_list = []
        address_value = 0
        if len(strings) == 1:
            if strings[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key in models.storage.all().keys():
                    class_name = key.split('.')
                    if class_name[0] == strings[0]:
                        new_list.append(str(models.storage.all()[key]))
                    else:
                        continue
                print(new_list)
        else:
            for key, value in models.storage.all().items():
                new_list.append(str(models.storage.all()[key]))
            print(new_list)

    def do_update(self, args):
        '''update an instance
           Usage update <class name> <id> <attribute name> "<attribute value>"
        '''
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            key_find = args[0] + '.' + args[1]
            if key_find not in objects:
                print('** no instance found **')
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) >= 4:
            obj = objects[args[0] + '.' + args[1]]

            if args[2] in obj.__dict__:
                val_type = type(obj.__dict__[args[2]])
                obj.__dict__[args[2]] = eval(args[3])
            else:
                obj.__dict__[args[2]] = eval(args[3])

        models.storage.save()

    def do_quit(self, args):
        '''<Quit> Command To Exit The Program'''
        return True

    def do_EOF(self, args):
        '''Handles end of file'''
        return True

    def do_help(self, args):
        '''help'''
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        '''dont execute anything when user
           press enter an empty line
        '''
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()