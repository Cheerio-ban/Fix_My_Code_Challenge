#!/usr/bin/python3
""" User class """


class User:
    """ Represents a User class """
    def __init__(self):
        """ Initializes the attributes """
        self.__email = None

    @property
    def email(self):
        """ Documentation """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets private attrbute of square class """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    """Creates an instance of the class"""
    u = User()
    u.email = "john@snow.com"
    print(u.email)
