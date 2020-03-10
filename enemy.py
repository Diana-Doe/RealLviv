'''Module with class Enemy'''
class Enemy:
    '''Represents Enemy'''
    def __init__(self, name, health, attack):
        '''
        str, int, int -> None
        '''
        self.name = name
        self.health = health
        self.attack = attack
        self.description = ''

    def set_description(self, description):
        '''
        str -> None
        Set description for enemy
        '''
        self.description = description

    def damage(self, damage):
        '''
        int -> None
        Bit enemy with some damage
        '''
        self.health = self.health - damage
