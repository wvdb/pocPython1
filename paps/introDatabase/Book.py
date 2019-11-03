__author__ = 'wim van den brande'

class Book:
    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self, *args, **kwargs):
        return "Book{" + ", name='" + self.name + "'" + ", description='" + self.description + "'" + "}"




