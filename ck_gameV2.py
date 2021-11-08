# Marceia Patterson
# 11/1/21


from ck_roomsV2 import Room


class Game:
    """
    11.1.21
    Basic game functions work (go NSEW, etc.)
    Need to add other rooms and items (keys).
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        #self.player = player.Player()
        self.rooms = { } # stored in dictionary
        self.here = None # TODO: move this to Player
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
     

    def __str__(self):
        pass

    def __repr__(self):
        pass



#Rooms needed: Red, Orange, Yellow, Green, Blue, Purple, and START/Main



    def setup(self):
       """ setup(): create a graph of rooms for play. """

        
       redRoom = Room( "Red Room", 
                   "This room smells like cherries.",
                   {"east":"Black and White Room",
                   "south": "Yellow Room"} )
    
        
       ylwRoom = Room ( "Yellow Room",
                           "There's a bowl of bananas on the table.",
                           { "east" : "Blue Room",
                             "north" : "Red Room"} )
        
       bluRoom = Room ( "Blue Room", 
                         "The windows show the clear skies.",
                         { "north" : "Black and White Room",
                          "west" : "Yellow Room"} )
        
       bwRoom = Room ( "Black and White Room", 
                     "There's bizarre contrasting art on the walls.",
                     { "west" : "Red Room",
                      "south" : "Blue Room"})
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
       self.rooms = { redRoom.name: redRoom, 
                ylwRoom.name: ylwRoom,
                bluRoom.name: bluRoom,
                bwRoom.name: bwRoom}
        
       self.here = redRoom # starting location

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            self.commandGo(direction)    
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")
        elif verb == "get":
            item = words[1]
            self.commandGet(item)
        elif verb == "drop":
            item = words[1]
            self.commandDrop(item)
        
        else: # first word is verb
            print("I don't know how to", words[0])

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        # Can we go in the chosen direction from here?
        if self.here.exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            newRoomName = self.here.exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        # TODO: actually do this
        # We'll need to remove the item from the current
        # room, and then add it to the player inventory
        # (which means we need a player inventory)
        print("You try to get the", itemName)

        
        if self.here.contains(itemName):
            item = self.here.contents[itemName]
            self.here.moveItemTo(item, self.player)
            print("You pick up the ",itemName,".")
        else:
            print("You can't see any", itemName, "here.")
        
 
    def commandDrop(self, itemName):
        """ remove the item from player inventory
        (if it's there) and add it to the room. 
        """
        print("You try to drop the", itemName)
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have a", itemName, "to drop!")



def main():
    game = Game()
    game.setup()
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
