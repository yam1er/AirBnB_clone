#!/usr/bin/python3
"""Defines a review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review

    Attributes:
        place_id: string
        user_id: string
        text: string
    """
    place_id = ""
    user_id = ""
    text = ""
