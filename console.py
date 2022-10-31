#!/usr/bin/env python3
""" The console: A command interpreter implemented from class Cmd """


import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ class inheriting from the Cmd class
        Attributes:
            prompt (str): a prompt to take input commands from user

            intro (str): A text displayed before the prompt when the
            console is run

        Methods:
            do_EOF: method to implement the End Of File and exit the program

            do_quit: method to quit the program
    """
    prompt = "(hbnb)"

    def emptyline(self):
        """ method to do nothing when an empty line is parsed """

        pass

    def do_quit(self, line):
        """ command to quit the program """
        print()

        return True

    def do_EOF(self, line):
        """ this method recognises CTRL D and quits the program """
        print()

        return True

    def do_create(self, line):
        """ creates a new instance of BaseModel"""

        if not line:
            print("** class name missing **")

        elif line != "BaseModel":
            print("** class doesn't exist **")

        else:
            new_model = BaseModel()
            print(new_model.id)
            new_model.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
