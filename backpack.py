'''Module with class Backpack'''

class Backpack:
    '''class for backpack representation'''
    def __init__(self):
        '''
        None -> None
        '''
        self.contents = []

    def set_contents(self, item):
        '''
        Item -> None
        Add item to backpack
        >>> backpack = Backpack()
        >>> backpack.set_contents('candy')
        >>> print(backpack.contents)
        ['candy']
        '''
        self.contents.append(item)
