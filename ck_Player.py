# Player class

from ck_Container import Container

class Player(Container):
    """
    Any data relating to the player himself should go in the 
    Player class.
    Examples: location, inventory, health status, etc. etc.
    
    TODO: add player flag dictionary
    
    """
    
    def __init__(self):
        self._loc = None # what room is the player in?
        self.contents = {} # because we're also a container
    
    
    #please work 