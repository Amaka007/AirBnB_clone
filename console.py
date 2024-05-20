#!/usr/bin/env python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class that defines commands to manage the AirBnB clone project.
    """
    prompt = '(hbnb) '

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
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
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
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name, id, attribute_name, attribute_value = args[0], args[1], args[2], args[3].strip('"')
        key = f"{class_name}.{id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]
        try:
            cast_type = type(getattr(obj, attribute_name))
            attribute_value = cast_type(attribute_value)
        except AttributeError:
            pass
        setattr(obj, attribute_name, attribute_value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

