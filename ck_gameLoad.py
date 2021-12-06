# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:47:41 2021

@author: MarceiaP
"""

from ck_game import Game
from ck_rooms import Room
from ck_Player import Player
from ck_Items import Item

class MyGame(Game):
    """ the Game class should be subclassed to add
    game specific features, including the world setup. 
    """
    
    def setup(self):
        """ Load your own rooms in the method of your choosing.
        Consider a GameLoader class that might read these
        from a file...
        """
        loader = MyGameLoader()
        self.rooms = loader.setup()
        
        # starting location
        self.here = self.rooms["Main Room"]
        # Let's do a turn 1 look , to orient the player
        self.here.describe()
        
        

class MyGameLoader:
    """ just used to put all the room setup in a separate class,
    and if needed, a separate file.
    """
    def setup(self):
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
    
    
        roomDict = {
                     mainRoom.name: mainRoom,
                     redRoom.name: redRoom,
                     orgRoom.name: orgRoom,
                     ylwRoom.name: ylwRoom,
                     grnRoom.name: grnRoom,
                     bluRoom.name: bluRoom,
                     purRoom.name: purRoom }
                    
        return roomDict 
        
        
# Startup
def main():
    game = MyGame()
    game.setup()
    game.output("Starting game -- enter command.")
    game.loop()
    game.end()


if __name__ == "__main__":
    main()