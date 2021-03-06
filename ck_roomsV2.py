# CSC 221
# M3LAB1 - TextAdv prototype
# Marceia Patterson
# 10/12/21


#from Container import Container

class Room:
    """
    The Room class holds names, descriptions, and exits.
    In future it should also manage objects in rooms, somehow
    v3 - 10/4/21
    """

        
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def __str__(self):
        """ contains the name, description, and exits in a human-readable fashion"""
        text = self.name + "\n"
        text += self.description + "\n"
        # append all exits
        exitList = self.exits.keys() # this gives us a list of all directions ipresent in exits
        for direction in exitList:
            text += direction                     # North, South, etc. 
            text += ": " + self.exits[direction]  # prints in format "North: Living Room", etc.
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
            
            



def main():
    """
    Currently used for testing.
    TODO: uimplement doctests. """
    redRoom = Room( "Red Room", 
                   "The room smells like fresh cherries.",
                   {"south": "Yellow Room"} )
    
    #print(bedroom)
    
    ylwRoom = Room ( "Yellow Room",
                       "I smell a bunch of bananas.",
                       { "east" : "Blue Room" } )
    #print(livingRoom)
    
    bluRoom = Room ( "Blue Room", 
                     "Smells like someone made a blueberry pie.",
                     { "north" : "Black and White Room" } )
    
    endRoom = Room ( "Black and White Room", 
                     "You made it to the end. Congrats!",
                     { "north" : "Red Room" })
    
    # Place rooms in a dictionary.
    # (Game will handle this in the full version)
    roomDict = { redRoom.name: redRoom, 
                ylwRoom.name: ylwRoom,
                bluRoom.name: bluRoom,
                endRoom.name: endRoom}
    
    # Test out movement
    loc = redRoom
    print("Starting room:")
    loc.describe()
    
    print ("Heading South...")
    loc = roomDict[loc.exits["south"]] # find room to South, go there
    loc.describe()
    
    print ("Heading East...")
    loc = roomDict[loc.exits["east"]] # find room to North, go there
    loc.describe()
    
    print ("Heading North...")
    print("To the north is the red room again. You're in a loop.")

    
if __name__ == "__main__":
    main()
