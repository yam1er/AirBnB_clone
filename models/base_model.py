#!/usr/bin/python3
"""
  BaseModel Module
"""
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """
      BaseModel Class
    """
    def __init__(self, *args, **kwargs):
        """
          Instance Creation Method
        """
        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                print(key, value)
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self.to_dict())

    def __str__(self):
        """
          __str__ method
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
          Save Updates
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
          To Dict method
        """
        dict = self.__dict__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        dict.update({'__class__': self.__class__.__name__})
        return dict
