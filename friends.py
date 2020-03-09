from item import Item

class Friend():
    def __init__(self, name, action = True):
        self.name = name
        self.dialogue = ''
        self.action = action
        self.gift = None
        self.required = None
        self.text = None
    
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
    
    def talk(self):
        return self.dialogue

    def set_answer(self, required, text):
        self.required = required
        self.text = text
    
    def answer(self, item):
        return self.required
    
    def set_gift(self, gift):
        self.gift = gift

