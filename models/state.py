#!/usr/bin/python3
"""Defines the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represente a state

    Attributes:
        name (str): The name of the state
    """
    name = ""
