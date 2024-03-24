#!/usr/bin/python3
"""
  File Storage Module
"""
import json
import os


class FileStorage:
    """
      FileStorage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
          Returns dictionary of all object
        """
        return self.__objects

    def new(self, obj):
        """
          Add obj to objects
        """
        ob = obj.to_dict()
        key = ob["__class__"] + "." + ob["id"]
        self.__objects[key] = ob

    def save(self):
        """
          Serialize objects to JSON file
        """
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
          Deserialize JSON file to objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                self.__objects = json.load(file)

    def delete(self, key):
        """
          Remove an object from __objects and save
        """
        del self.__objects[key]
        self.save()
