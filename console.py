#!/usr/bin/env python3
""" The console: A command interpreter implemented from class Cmd """


import cmd
from models import storage
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

    @staticmethod
    def check_class(line):
        """ method to confirm class is present and exist """

        arg_list = line.split()

        if len(arg_list) < 1:
            print("** class name missing **")
            return False

        elif arg_list[0] != "BaseModel":
            print("** class doesn't exist **")
            return False

        else:
            return True

    @staticmethod
    def check_id(line):
        arg_list = line.split()

        if len(arg_list) < 2:
            print("** instance id missing **")
            return False

        objs = storage.all()
        key = "{}.{}".format(arg_list[0], arg_list[1])
        if key not in objs.keys():
            print("** no instance id found **")
            return False
        else:
            return True

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

        if self.check_class(line) is True:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """ prints the string representtion of an instance based on id """

        if (self.check_class(line) is False) or (self.check_id(line) is False):
            return

        objs = storage.all()
        args = line.split()
        key = "{}.{}".format(args[0], args[1])
        string = objs[key].__str__()
        print(string)

    def do_destroy(self, line):
        """ delets an instance of a class """

        if (self.check_class(line) is False) or (self.check_id(line) is False):
            return
        args = line.split()
        key = "{}.{}".format(args[0], args[1])
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """" prints __str__ of all instances based or not on class"""

        if len(line.split()) == 0:
            objs = storage.all()
            for key, value in objs.items():
                print(value.__str__())
            return

        if self.check_class(line) is False:
            return

        objs = storage.all()
        for key, value in objs.items():
            if isinstance(value, BaseModel):
                print(value.__str__())

    def do_update(self, line):
        """ updates the attributes of an instance """

        if (self.check_class(line) is False) or (self.check_id(line) is False):
            return

        if len(line.split()) < 3:
            print("** attribute name missing **")
            return

        if len(line.split()) < 4:
            print("** value missing **")
            return

        objs = storage.all()
        args = line.split()
        anchor = "{}.{}".format(args[0], args[1])
        if anchor in objs.keys():
            setattr(objs[anchor], args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
