# CSC 221
# M3LAB1 - TextAdv prototype
# Marceia Patterson
# 10/12/21


from ck_Items import Item
from ck_Container import Container

class Room(Container):
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    v3 - 10/4/21
    """

        
    def __init__(self, name, description, exits):
        self._name = name
        self._description = description
        self._exits = exits
        self._contents = {} # used by container

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self._name + "\n"
        text += self._description + "\n"
        # append all exits
        exitList = self._exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self._exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
        return text

 #   def __repr__(self):  # we're not using this yet
 #       pass


    def describe(self):
        """ print full room description. """
        print(self)
    
    def exit(self, direction):
        """
        input: an exit direction, as string
        output: a Room object - either the room the player
            has moved to, or the current room if
            movement failed.
        """   
        pass 
        # I need access to the roomDict for this -- so it should 
        # go in Game, not Room.             
            
    def addItem(self, item):
        """ used to add an item into a room. """
        self.add(item)
    
    def removeItem(self, item):
        """ used to remove items from a room. """
        self.remove(item)       




#ALL USED FOR TESTING. ENABLED WILL BREAK CODE
#VVVVVVVVV
# =============================================================================
# #used for testing
# def main():
# 
#     mainRoom = Room("You wake up in a dark room. Before you is a large door with six key holes. Maybe it's a way out.",
#                        {"north":"Red Room",
#                         "south":"Green Room",
#                         "east":"Blue Room",
#                         "west":"Yellow Room"}) 
#        
#     redRoom = Room( "Red Room", 
#                    "Crismon roses sprout out of cracks in the walls.",
#                        {"south":"Main Room",
#                         "east":"Purple Room",
#                         "west":"Orange"})
#        
#     orgRoom = Room( "Orange Room", 
#                    "An essence of citrus fills the air.",
#                        {"south":"Yellow Room",
#                         "east":"Red Room"})
#         
#     ylwRoom = Room ( "Yellow Room",
#                            "There's a bowl of bananas on the table.",
#                            {"south":"Main Room",
#                             "east":"Purple Room",
#                             "west":"Orange"})
#        
#     grnRoom = Room( "Green Room", 
#                    "You gag at the smell of pungency as you trod through the slime-coated floors.",{"north":"Main"})
#         
#     bluRoom = Room ( "Blue Room", 
#                          "The windows show the clear skies.",
#                          { "north" : "Purple",
#                           "west" : "Main Room"})
#         
#     purRoom = Room ( "Purple Room", 
#                      "Asatin violet love seat is placed beside a vase of lilacs.",
#                      { "west" : "Red Room",
#                       "south" : "Blue Room"})
#     
#     # Place rooms in a dictionary.
#     # (Game will handle this in the full version)
#     roomDict = { mainRoom.name: mainRoom,
#                 redRoom.name: redRoom,
#                 orgRoom.name: orgRoom,
#                 ylwRoom.name: ylwRoom,
#                 grnRoom.name: grnRoom,
#                 bluRoom.name: bluRoom,
#                 purRoom.name: purRoom}
#     
#     
#     
#     # Test out items
#     key = Item("key", "It's a bit rusty.")
#     sword = Item("sword", "It's very shiny.")
#     mainRoom.addItem(key)
#     redRoom.addItem(sword)
#     #print(loc.contents) # just dump the list
#     
#     
#     # Test out movement
#     loc = mainRoom
#     print("Starting room:")
#     loc.describe()
#     
#     print ("Heading South...")
#     loc = roomDict[loc.exits["south"]] # find room to South, go there
#     loc.describe()
#     
#     print ("Heading East...")
#     loc = roomDict[loc.exits["east"]] # find room to North, go there
#     loc.describe()
#     
#     print ("Heading North...")
#     print("To the north is the red room again. You're in a loop.")
# 
#  
#     if __name__ == "__main__":
#   main()   
# =============================================================================

