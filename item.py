class Item:
    def __init__(self, name):
        '''
        str -> None
        '''
        self.name = name
        self.description = ''
    
    def set_description(self, description):
        '''
        str -> None
        '''
        self.description = description
    
    def take(self):
        return self.name
    
class Weapon(Item):
    def __init__(self, name, damage):
        Item.__init__(self, name)
        self.damage = damage

    def set_description(self, description):
        Item.set_description(self, description)
    
    def take(self):
        super().take()
    
    