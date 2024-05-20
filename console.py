#!/usr/bin/env python3
"""
This module contains the entry point for the command interpreter.
"""

import cmd

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

    def do_help(self, arg):
        """
        Provides help information for commands.
        """
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                    return
            func()
        else:
            cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

