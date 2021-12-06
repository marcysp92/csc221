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
    
    #super runs the equiv function from the base class
    def __init__(self, name, description):
        super().__init__(name, description)
        
        
class UsableItem (Item):
    """
    Works like a regular item, except that
    it has one or more usable verbs
    that will cause it to make changes.
    """
    def __init__(self, name, description):
        super().__init__(name, description)
        self._wasUsed = False
        
    def use(self, useVerb = "use"):
        
        if self._wasUsed == True:
            print("You already used this item.")
        else:
            print("You attempt to",useVerb,"the item.")
            self._wasUsed = True
            
            
    @property
    def description(self):
        """return a decorated description. 
        Decoration = things like (too heavy to lift)
        This example just polishes the object.""" 
        desc = self._description
        # decorate with extra info as needed
        if self._wasUsed == True:
            desc += " Item was used."
        else:
            desc += " Item was not used."
        return desc
        


# Test code
"""
List of items needed:
    Red Key, Orange Key, Yellow Key, Green Key, Blue Key, Purple Key.
    R,Y,B key are provided in the corresponding rooms. 
    Combine two keys to access another in a locked room.
"""

def main():
    redKey = Item("Red Key", "Looks shinier than a ruby.")
    
    orgKey = Item("Orange Key", "Orange you glad I had the red and yellow key?")

    
    ylwKey = Item("Yellow Key", "Its hue is as radiant as the sun.")
    
    grnKey = Item("Green Key", "Guess things are greener on the other side.")
    
    bluKey = Item("Blue Key", "Looks cool and clear like the ocean.")
    
    purKey = Item("Purple Key", "It's more beautiful than red and blue combined.")
    
    stuff = [redKey, orgKey, ylwKey, grnKey, bluKey, purKey]
    for item in stuff:
        print(item.name, "-", item.description)
    #This works!! :D    
    
    #redKey = UsableItem("Red Key", "Looks shinier than a ruby.")
    
    #redKey.use()
    #for item in stuff:
       #print(item.name, "-", item.description)
if __name__ == "__main__":
    main()