#!/usr/bin/python3
"""
  BaseModel Module
"""
import datetime
import uuid

class BaseModel:
    """
      BaseModel Class
    """
    def __init__(self):
        """
          Instance Creation Method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
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

    def to_dict(self):
        """
          To Dict method
        """
