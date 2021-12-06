# CSC 221
# M3LAB1 - TextAdv prototype
# Marceia Patterson
# 10/17/21


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
        self.contents = {} # used by container
        self.locked = False

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        "Items are now listed in each corresponding room."
        text = self._name + "\n"
        text += self._description + "\n"
        text += "In this room you see: \n"
        text += self.listContents()
        # append all exits
        exitList = self._exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self._exits[direction]  # prints in format "North: Living Room", etc.
            text += "\n"
            # print items in room, if any
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
        
    def lock(self):
        if self.locked == True:
            
            print("The room is locked. Looks like it needs two keys to open.")
    
    def unlock(self):
        pass
        if self.locked == False:
            print("The room is unlocked. Let's go inside!")
    
    
def main():
    #Linking items to Rooms
    """
    ROOM DIRECTIONS:
        MAIN - N:Red, S: Green, E: Blue, W: Yellow
        Red - N: Nothing, S: Main, E: Purple, W: Orange
        Orange - N: Nothing, S: Yellow, E: Red, W: Nothing
        Yellow - N: Orange, S: Nothing, E: Main, W: Nothing
        Green - N: Main, S: Nothing, E: Nothing, W: Nothing
        Blue - N: Purple, S: Nothing, E: Nothing, W: Main
        Purple - N: Nothing, S: Blue, E: Nothing, W: Red
        
    """
    mainRoom = Room( "Main Room","You are in a darkened room with a large door.",
                       {"north":"Red Room",
                        "south":"Green Room",
                        "east":"Blue Room",
                        "west":"Yellow Room"}) 
    
    redRoom = Room( "Red Room", 
                    "Crismon roses sprout out of cracks in the walls.",
                        {"south":"Main Room",
                        "east":"Purple Room",
                         "west":"Orange"})
        
    orgRoom = Room( "Orange Room", 
                    "An essence of citrus fills the air.",
                        {"south":"Yellow Room",
                         "east":"Red Room"})
         
    ylwRoom = Room ( "Yellow Room",
                            "There's a bowl of bananas on the table.",
                            {"south":"Main Room",
                             "east":"Purple Room",
                             "west":"Orange"})
        
    grnRoom = Room( "Green Room", 
                    "You gag at the smell of pungency as you trod through the slime-coated floors.",{"north":"Main"})
         
    bluRoom = Room ( "Blue Room", 
                          "The windows show the clear skies.",
                          { "north" : "Purple",
                           "west" : "Main Room"})
         
    purRoom = Room ( "Purple Room", 
                     "Asatin violet love seat is placed beside a vase of lilacs.",
                      { "west" : "Red Room",
                      "south" : "Blue Room"})

    #Adding Links
    redKey = Item("Red Key", "Looks shinier than a ruby.")
    redRoom.addItem(redKey)
    
    orgKey = Item("Orange Key", "Orange you glad I had the red and yellow key?")
    orgRoom.addItem(orgKey)
    
    ylwKey = Item("Yellow Key", "Its hue is as radiant as the sun.")
    ylwRoom.addItem(ylwKey)
    
    grnKey = Item("Green Key", "Guess things are greener on the other side.")
    grnRoom.addItem(grnKey)
    
    bluKey = Item("Blue Key", "Looks cool and clear like the ocean.")
    bluRoom.addItem(bluKey)
    
    purKey = Item("Purple Key", "It's more beautiful than red and blue combined.")
    purRoom.addItem(purKey)


    roomDict = { mainRoom.name: mainRoom,   
                 redRoom.name: redRoom,
                 orgRoom.name: orgRoom,
                 ylwRoom.name: ylwRoom,
                 grnRoom.name: grnRoom,
                 bluRoom.name: bluRoom,
                 purRoom.name: purRoom }

    loc = mainRoom
    print("Starting Room:")
    loc.describe()
    
    print("Heading South...")
    loc = roomDict[loc.exits["south"]]
    loc.describe()
    





#ALL USED FOR TESTING. UNCOMMENTED WILL BREAK CODE!!!
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
    if __name__ == "__main__":
        main()   
