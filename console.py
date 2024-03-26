#!/usr/bin/python3
"""
  Conlose Module
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


c = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']


class HBNBCommand(cmd.Cmd):
    """
      The console main class
    """
    prompt = '(hbnb) '

    def default(self, line):
        """
          Default command
        """
        cls, call = line.split(".")
        method, args = call.split("(")
        if method == "all":
            self.do_all(cls)
        elif method == "count":
            self.do_all(cls)
        elif method == "show":
            args = args.strip('()').strip('""')
            self.do_show(cls + " " + args)

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
        elif line[0] not in c:
            print("** class doesn't exist **")
        else:
            if line[0] == 'BaseModel':
                obj = BaseModel()
            elif line[0] == 'User':
                obj = User()
            elif line[0] == 'State':
                obj = State()
            elif line[0] == 'City':
                obj = City()
            elif line[0] == 'Amenity':
                obj = Amenity()
            elif line[0] == 'Place':
                obj = Place()
            elif line[0] == 'Review':
                obj = Review()
            print(obj.id)
            obj.save()

    def do_show(self, line):
        """Print string rep of an instance
        """
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in c:
            print("** class doesn't exist **")
        elif (len(line) > 1 and line[1] == "") or len(line) == 1:
            print("** instance id missing **")
        else:
            key = line[0] + "." + line[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                if line[0] == 'BaseModel':
                    obj = BaseModel(**storage.all()[key])
                elif line[0] == 'User':
                    obj = User(**storage.all()[key])
                elif line[0] == 'State':
                    obj = State(**storage.all()[key])
                elif line[0] == 'City':
                    obj = City(**storage.all()[key])
                elif line[0] == 'Amenity':
                    obj = Amenity(**storage.all()[key])
                elif line[0] == 'Place':
                    obj = Place(**storage.all()[key])
                elif line[0] == 'Review':
                    obj = Review(**storage.all()[key])
                print(obj)

    def do_all(self, line):
        """Print all object of a class or all objects
        """
        line = line.split(" ")
        if line[0] == "":
            all = []
            for key, value in storage.all().items():
                if value['__class__'] == 'BaseModel':
                    rep = BaseModel(**storage.all()[key]).__str__()
                elif value['__class__'] == 'User':
                    rep = User(**storage.all()[key]).__str__()
                elif value['__class__'] == 'State':
                    rep = State(**storage.all()[key]).__str__()
                elif value['__class__'] == 'City':
                    rep = City(**storage.all()[key]).__str__()
                elif value['__class__'] == 'Amenity':
                    rep = Amenity(**storage.all()[key]).__str__()
                elif value['__class__'] == 'Place':
                    rep = Place(**storage.all()[key]).__str__()
                elif value['__class__'] == 'Review':
                    rep = Review(**storage.all()[key]).__str__()
                all += [rep]
            print(all)
        elif line[0] in c:
            all = []
            for key, value in storage.all().items():
                keys = key.split(".")
                if keys[0] == line[0]:
                    if value['__class__'] == 'BaseModel':
                        rep = BaseModel(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'User':
                        rep = User(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'State':
                        rep = State(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'City':
                        rep = City(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'Amenity':
                        rep = Amenity(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'Place':
                        rep = Place(**storage.all()[key]).__str__()
                    elif value['__class__'] == 'Review':
                        rep = Review(**storage.all()[key]).__str__()
                    all += [rep]
            print(all)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Destroy an instance an save to JSON
        """
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in c:
            print("** class doesn't exist **")
        elif (len(line) > 1 and line[1] == "") or len(line) == 1:
            print("** instance id missing **")
        else:
            key = line[0] + "." + line[1]
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.delete(key)

    def do_update(self, line):
        """Update an instance attribute and save
        """
        line = line.split(" ")
        if line[0] == "":
            print("** class name missing **")
        elif line[0] not in c:
            print("** class doesn't exist **")
        elif (len(line) > 1 and line[1] == "") or len(line) == 1:
            print("** instance id missing **")
        elif line[0] + "." + line[1] not in storage.all().keys():
            print("** no instance found **")
        elif (len(line) > 2 and line[2] == "") or len(line) == 2:
            print("** attribute name missing **")
        elif (len(line) > 3 and line[3] == "") or len(line) == 3:
            print("** value missing **")
        else:
            key = line[0] + "." + line[1]
            storage.all()[key][line[2]] = line[3]
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
