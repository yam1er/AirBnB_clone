#!/usr/bin/python3
"""
  Conlose Module
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
      The console main class
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End the program running
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
          Handle empty line
        """
        return False

    def do_create(self, line):
        """Create and save objects
        """
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
