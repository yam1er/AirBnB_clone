#!/usr/bin/python3
"""
  BaseModel Module
"""
import datetime
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
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            "Creation from dict"
            print("Implement it")
        
    def __str__(self):
        """
          __str__ method
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
          Save Updates
        """
        self.updated_at = datetime.datetime.now()
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
