#!/usr/bin/python3
"""
  File Storage Module
"""
import JSON


class FileStorage:
    """
      FileStorage Class
    """
    __file_path = ""
    __objects = []

    def all(self):
        """
          Returns dictionary of all object
        """
        return FileStorage.__objects

    def new(self, obj):
        """
          Add obj to objects
        """
        FileStorage.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
          Serialize objects to JSON file
        """
        with open(self.__file_path, w, encoding='uft-8') as file:
            JSON.dump(self.__objects, file)

    def reload(self):
        """
          Deserialize JSON file to objects
        """
        with open(self.__file_path, r, encoding='utf-8') as file:
            JSON.load(self.__objects, file)
