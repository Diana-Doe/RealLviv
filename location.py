from place import Place

class Location:
    def __init__(self, name):
        self.name = name
        self.places = []
        self.locations = []
        self.description = None

    def set_places(self,places):
        '''
        list(Place) -> None
        '''
        self.places = places
    
    def set_description(self, description):
        '''
        str -> None
        '''
        self.description = description