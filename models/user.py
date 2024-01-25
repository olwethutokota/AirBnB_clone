#!/usr/bin/python3
''' class User that inherits from BaseModel '''

from models.base_model import BaseModel


class User(BaseModel):
    ''' .. ... '''
    # Define atributos para la creación de usuarios
    email = ""
    password = ""
    first_name = ""
    last_name = ""
