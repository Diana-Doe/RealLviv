'''Module with class Item'''
class Item:
    '''Class for item representation'''
    def __init__(self, name):
        '''
        str -> None
        '''
        self.name = name
        self.description = ''

    def set_description(self, description):
        '''
        str -> None
        Set description for item.
        >>> item = Item('Fanta')
        >>> item.set_description('A bottle of soda')
        >>> print(item.description)
        A bottle of soda
        '''
        self.description = description

class Weapon(Item):
    '''Represents weapon'''
    def __init__(self, name, damage):
        '''
        Str, int -> None
        '''
        Item.__init__(self, name)
        self.damage = damage

    def set_description(self, description):
        '''
        str -> None
        Set description for weapon
        >>> gun = Weapon('Gun', 90)
        >>> gun.set_description('Small gun')
        >>> print(gun.description)
        Small gun
        '''
        Item.set_description(self, description)
