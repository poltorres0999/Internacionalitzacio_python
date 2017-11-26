import gettext

class Person:

    def __init__(self, name, surname1, surname2, address, ID):
        self.name = name
        self.surname1 = surname1
        self.surname2 = surname2
        self.address = address
        self.ID = ID
        pass

    def print_person(self):
        print(_('Name: '), self.name + '\n')
        print(_('Surname1: '), self.surname1 + '\n')
        print(_('Surname2: '), self.surname2 + '\n')
        print(_('Address: '), self.address + '\n')
        print(_('ID: '), self.ID + '\n')




