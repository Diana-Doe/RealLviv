from termcolor import colored
import sys,time,random

def slow(text, speed):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        if speed == 1: time.sleep(0.08) #0.08
        else: time.sleep(0.02) #0.02

    print('')

class Place:
    def __init__(self, name, description, blocked=False):
        '''
        str, str -> None
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
        '''
        self.persons.append(person)

    def set_item(self, item):
        '''
        Item -> None
        '''
        self.item.append(item)
    
    def set_place(self, place):
        self.locations.append(place)
    
    def get_item(self):
        return self.item
    
    def get_person(self):
        return self.persons

    def get_locations(self):
        return self.locations

    def get_details(self):
        slow(self.name, 1)
        print('___________________')
        slow(self.description, 2)
        st = []
        if len(self.locations) != 0:
            for i in self.locations:
                st.append(i.name)
            slow('[backpack]: open backpack', 2)
            slow('[exit]: exit', 2)
            slow('[leave]: {}'.format(colored(', '.join(st), 'green')), 1)