#!/usr/bin/env python3
"""Console module for the AirBnB clone project."""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the AirBnB clone project.
    """
    prompt = "(hbnb) "

    def do_help(self, arg):
        """ Help command to get help on <topic> """
        return super().do_help(arg)

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        
        Args:
            arg: Additional arguments (not used).
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        
        Args:
            arg: Additional arguments (not used).
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command when an empty line is entered.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

