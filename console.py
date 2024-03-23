#!/usr/bin/python3
"""
  Conlose Module
"""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
