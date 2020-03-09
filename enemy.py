class Enemy:
    def __init__(self, name, health, attack):
        '''
        str, name
        '''
        self.name = name
        self.health = health
        self.attack = attack
        self.description = ''
    
    def set_description(self, description):
        self.description = description
    
    def damage(self, damage):
        self.health = self.health - damage
    