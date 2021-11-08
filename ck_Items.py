# Item class

class BaseItem:
    def __init__(self, name, description):
        self._name = name
        self._description = description
        
        self._canGet = True
        
    def __str__(self):
        return self._name + " : " + self._description
    
    @property 
    def name(self):
        return self._name 

    @property
    def description(self):
        desc = self._description
        
        if self._canGet == False:
            desc += " Cannot pick up item"
        return desc
    
    @property
    def canGet(self):
        return self._canGet
    
    
    @canGet.setter  
    def canGet(self, setting):
        """True/False item pickup"""
        self._canGet = setting
    
class Item (BaseItem):
    
     #super runs the equic function from the base class
    def __init__(self, name, description):
        super().__init__(name, description)
        
        
class UsableItem (Item):
    """
    
    """
    def __init__(self, name, description):
        super().__init__(name, description)
        self._wasUsed = False
        
    def use(self, useVerb = "use"):
        """
        use() - call to make objec change to its other state.
        TODO: this needs more though
        
        Parameters
        ----------
        useVerb : TYPE, optional
            DESCRIPTION. The default is "use".

        Returns
        -------
        None.

        """
        
        
        
        

# Test code
"""
List of items needed:
    Red Key, Orange Key, Yellow Key, Green Key, Blue Key, Purple Key.
    R,Y,B key are provided in the corresponding rooms. 
    Combine two keys to access another in a locked room.
"""
def main():
    key = Item("key", "It's a bit rusty.")
    
    sword = Item("sword", "It's very shiny.")
    
    bed = Item("Bed", "Looks soft.")
    bed.canGet = False
    
    stuff = [key, sword, bed]
    for item in stuff:
        print(item.name, "-", item.description)
        
if __name__ == "__main__":
    main()