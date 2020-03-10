'''Module with function slow and class Person'''

import sys
import time
from clint.textui import colored

def slow(text, speed):
    '''
    Function that print text slowly. Has 2 modes of speed.
    '''
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        if speed == 1:
            time.sleep(0.08) #0.08
        else:
            time.sleep(0.02) #0.02

    print('')

class Place:
    '''
    Represents locations for game.
    '''
    def __init__(self, name, description, blocked=False):
        '''
        str, str -> None
        Every place has unique name, description. Some places are blocked at the beggining.
        >>> park = Place('Mansfield Park', 'Park from  Jane Austen novel')
        >>> print(park.name)
        Mansfield Park
        >>> print(park.blocked)
        False
        '''
        self.name = name
        self.description = description
        self.persons = []
        self.item = []
        self.locations = []
        self.blocked = blocked

    def set_person(self, person):
        '''
        Person -> None
        >>> park = Place('Mansfield Park', 'Park from  Jane Austen novel')
        >>> park.set_person('Fanny Price')
        >>> park.persons
        ['Fanny Price']
        '''
        self.persons.append(person)

    def set_item(self, item):
        '''
        Item -> None
        Put intem into location.
        '''
        self.item.append(item)

    def set_place(self, place):
        '''
        Place ->
        Set near location. Put it in list.
        '''
        self.locations.append(place)

    def get_item(self):
        '''
        None -> Item
        Return list of items.
        '''
        return self.item

    def get_person(self):
        '''
        Return list of persons.
        '''
        return self.persons

    def get_locations(self):
        '''
        None -> list
        Return list with near locations
        '''
        return self.locations

    def get_details(self):
        '''
        None -> None
        Print description of location.
        '''
        slow(self.name, 1)
        print('___________________')
        slow(self.description, 2)
        string = []
        if self.locations:
            for i in self.locations:
                string.append(i.name)
            slow('[backpack]: open backpack', 2)
            slow('[exit]: exit', 2)
            slow('[leave]: {}'.format(colored.green(', '.join(string))), 1)
