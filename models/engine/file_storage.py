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
        return FileStorage.__objects

    def new(self, obj):
        """
          Add obj to objects
        """
        key = obj["__class__"] + "." + obj["id"]
        FileStorage.__objects.update({key: obj})

    def save(self):
        """
          Serialize objects to JSON file
        """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
          Deserialize JSON file to objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                FileStorage.__objects = json.load(file)
