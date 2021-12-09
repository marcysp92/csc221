# Marceia Patterson
# 11/17/21
# Color Keys v4


from ck_rooms import Room
from ck_Player import Player
from ck_Items import Item



class Game():
    """
    11.17.21
    Rooms work! :D
    Now we need to work on item management (pick up, drop, save in inventory, etc.)
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        self.rooms = { } # stored in dictionary
        # Player is currently used to hold current location (loc)
        self.player = Player() 
        
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
     

    def __str__(self):
        pass

    def __repr__(self):
        pass



#Rooms needed: Red, Orange, Yellow, Green, Blue, Purple, and START/Main

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

    def setup(self):
       """ setup(): create a graph of rooms for play. """

       mainRoom = Room( "Main Room","You are in a darkened room with a large door.",
                       {"north":"Red Room",
                        "south":"Green Room",
                        "east":"Blue Room",
                        "west":"Yellow Room"}) 
       
       redRoom = Room( "Red Room", 
                   "Crismon roses sprout out of cracks in the walls.",
                       {"south":"Main Room",
                        "east":"Purple Room",
                        "west":"Orange Room"})
       
       orgRoom = Room( "Orange Room", 
                   "An essence of citrus fills the air.",
                       {"south":"Yellow Room",
                        "east":"Red Room"})
        
       ylwRoom = Room ( "Yellow Room",
                           "There's a bowl of bananas on the table.",
                           {"north":"Orange Room",
                            "east":"Main Room"})
       
       grnRoom = Room( "Green Room", 
                   "You gag at the smell of pungency as you trod through the slime-coated floors.",
                   {"north":"Main Room"})
        
       bluRoom = Room ( "Blue Room", 
                         "The windows show the clear skies.",
                         { "north" : "Purple Room",
                          "west" : "Main Room"})
        
       purRoom = Room ( "Purple Room", 
                     "A plush violet sofa is placed beside a vase of lilacs.",
                     { "west" : "Red Room",
                      "south" : "Blue Room"})
       
       
       #Keys for rooms
       redKey = Item("Red Key", "Looks shinier than a ruby.")
       
       orgKey = Item("Orange Key", "Orange you glad I had the red and yellow key?")
       
       ylwKey = Item("Yellow Key", "Its hue is as radiant as the sun.")
       
    
       grnKey = Item("Green Key", "Guess things are greener on the other side.")
       
       bluKey = Item("Blue Key", "Looks cool and clear like the ocean.")
       
       purKey = Item("Purple Key", "It's more beautiful than red and blue combined.")
       
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        
       #Linking items
       redRoom.addItem(redKey)
       orgRoom.addItem(orgKey)
       ylwRoom.addItem(ylwKey)
       grnRoom.addItem(grnKey)
       bluRoom.addItem(bluKey)
       purRoom.addItem(purKey)
       
       
       #Specifying locked/unlocked rooms
       
       
       self.rooms = { 
                mainRoom.name: mainRoom,
                redRoom.name: redRoom,
                orgRoom.name: orgRoom,
                ylwRoom.name: ylwRoom,
                grnRoom.name: grnRoom,
                bluRoom.name: bluRoom,
                purRoom.name: purRoom}
        
       #Rooms finally work
       
       #Need to specify locked/unlocked rooms.
       
       
        
       
       self.here = mainRoom # starting location
       
       return self.rooms 
   
    
    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing!")
        


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
        elif verb == "check":
            self.commandCheckInv()
        elif verb == "use":
            item = words[1]
            self.commandUse(item)
        
        else: # first word is verb
            print("I don't know how to", words[0])

    def commandGo(self, direction):
        """ 
        input: direction to move.
        output: none
        side effect: player location is updated if possible.
        """
        # Can we go in the chosen direction from here?
        if self.here._exits.get(direction) == None:
            print("You can't go that way.")
        else:   
            # this key does exist
            newRoomName = self.here._exits[direction]
            newRoom     = self.rooms[newRoomName]
            self.here   = newRoom
            if self.isVerbose:
                self.here.describe()
    
    def commandGet(self, itemName):
        """ remove the item from the room (if it's there)
        and place it in player inventory.
        """
        #WHY WON"T THIS WORK?!! >:(
        #maybe have only one variable serving as the key to each room.
        #Ex. "Get key" triggers the Get and Drop function
        # lookup to fix the names - turn "red" into "Red Key" for example
        
        if itemName == "red":
            itemName = "Red Key"
        elif itemName == "blue":
            itemName = "Blue Key"
        elif itemName == "yellow":
            itemName = "Yellow Key"
        elif itemName == "green":
            itemName = "Green Key"
        elif itemName == "orange":
            itemName = "Orange Key"
        elif itemName == "purple":
            itemName = "Purple Key"
        # end fixing names
        print("You try to get the", itemName,".")
        
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
        if itemName == "red":
            itemName = "Red Key"
        elif itemName == "blue":
            itemName = "Blue Key"
        elif itemName == "yellow":
            itemName = "Yellow Key"
        elif itemName == "green":
            itemName = "Green Key"
        elif itemName == "orange":
            itemName = "Orange Key"
        elif itemName == "purple":
            itemName = "Purple Key"
        
        print("You try to drop the", itemName)
        
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.player.moveItemTo(item, self.here)
            print("You drop the", itemName,".")
        else:
            print("You don't have a", itemName, "to drop!")

    def commandCheckInv(self):
        print("INVENTORY")
        print("---------")
        itemNames = self.player.contents.keys()
        for itemName in itemNames:
            print(itemName)
    
    def commandUse(self, itemName):
        if self.player.contains(itemName):
            item = self.player.contents[itemName]
            self.here.moveItemTo(item, self.player)
            self.player.use(item, self.here)
            print("You used the", itemName,".")
        else:
            print("You can't use the", itemName, ".")
            
        #Add functionality to usable item

    # Helper functions -- not necessary, but useful
    @property
    def here(self):
        return self.player._loc
    
    @here.setter
    def here(self, room):
        self.player._loc = room


def main():
    game = Game()
    game.setup()
    print("Welcome to the Color Key game! -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
