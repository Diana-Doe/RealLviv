'''Module with class Friend'''
from item import Item

class Friend():
    '''Represents friend'''
    def __init__(self, name, action=True):
        '''
        str, bool -> None
        '''
        self.name = name
        self.dialogue = ''
        self.action = action
        self.gift = None
        self.required = None
        self.text = None

    def set_dialogue(self, dialogue):
        '''
        str -> None
        Set dialog with friend
        '''
        self.dialogue = dialogue

    def talk(self):
        '''
        None -> str
        Useless functiot.
        '''
        return self.dialogue

    def set_answer(self, required, text):
        '''
        Item, str -> None
        Set required for this scene item and dialogue.
        '''
        self.required = required
        self.text = text

    def answer(self):
        '''
        None -> None
        Return required for dialogue item.
        '''
        return self.required

    def set_gift(self, gift):
        '''
        Item -> None
        Set gift
        '''
        self.gift = gift
