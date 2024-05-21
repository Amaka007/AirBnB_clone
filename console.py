#!/usr/bin/env python3
"""
Command interpreter class for the AirBnB clone project
"""

import cmd
import re
import json
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class that defines commands to manage the AirBnB clone project.
    """
    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command on an empty line.
        Does nothing on an empty line + ENTER.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file), and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all or all <class name>
        """
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return

        objects = storage.all()
        obj_list = []
        if arg:
            for key, obj in objects.items():
                if key.startswith(arg):
                    obj_list.append(str(obj))
        else:
            for obj in objects.values():
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split(" ", 2)
        if not args[0]:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return

        # Check if the third argument is a dictionary
        if args[2].startswith("{") and args[2].endswith("}"):
            try:
                attr_dict = json.loads(args[2].replace("'", "\""))
            except json.JSONDecodeError:
                print("** invalid dictionary **")
                return
            for attr_name, attr_value in attr_dict.items():
                self.update_instance(key, attr_name, attr_value)
        else:
            attr_parts = args[2].split()
            if len(attr_parts) < 2:
                print("** value missing **")
                return
            attr_name = attr_parts[0]
            attr_value = attr_parts[1]
            self.update_instance(key, attr_name, attr_value)

    def update_instance(self, key, attr_name, attr_value):
        """Update instance helper to handle type conversion"""
        obj = storage.all()[key]
        if attr_value.isdigit():
            attr_value = int(attr_value)
        elif attr_value.replace('.', '', 1).isdigit():
            attr_value = float(attr_value)
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class"""

        l_arg = parse(arg)
        i = 0
        for obj in storage.all().values():
            if l_arg[0] == obj.__class__.__name__:
                i += 1
        print(i)

    def default(self, arg):
        """Override default method to handle custom commands"""
        parts = arg.split(".")
        if len(parts) == 2:
            class_name = parts[0]
            command = parts[1].strip("()")
            if command == "all":
                self.do_all(class_name)
            elif command == "count":
                self.do_count(class_name)
            elif command.startswith("show"):
                instance_id = command[5:-1].strip("\"")
                self.do_show(f"{class_name} {instance_id}")
            elif command.startswith("destroy"):
                instance_id = command[8:-1].strip("\"")
                self.do_destroy(f"{class_name} {instance_id}")
            elif command.startswith("update"):
                args = command[7:-1].split(", ", 1)
                if len(args) == 2:
                    instance_id = args[0].strip("\"")
                    if args[1].startswith("{") and args[1].endswith("}"):
                        self.do_update(f"{class_name} {instance_id} {args[1]}")
                    else:
                        parts_update = args[1].split(", ")
                        if len(parts_update) == 2:
                            attr_name = parts_update[0].strip("\"")
                            attr_value = parts_update[1].strip("\"")
                            self.do_update(f"{class_name} {instance_id} {attr_name} {attr_value}")
            else:
                print("** Unknown syntax: {}".format(arg))
        else:
            print("** Unknown syntax: {}".format(arg))

if __name__ == '__main__':
    HBNBCommand().cmdloop()

