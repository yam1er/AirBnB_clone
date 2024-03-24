#!/usr/bin/python3
"""
    Module for user class
"""
from models.base_module import BaseModel


class User (BaseModel):

    """

    class that represent a user

    Attributes;
    email: string
    password: string
    first_name: string
    last_name: string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
