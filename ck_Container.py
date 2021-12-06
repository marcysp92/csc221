# Container class
# should be able to add, remove, list, and 
# (optionally) transfer items
#
# we moved using a dictionary so we can easily
# do name lookups

from ck_Items import Item


class Container(Item):
    """ This class only handles collections of Items. """
    
    def __init__(self):
        self.contents = {}
        
    def add(self, item):
        self.contents[item.name] = item
        
    def remove(self, item):
        if self.contains(item.name):
            # remove the item from the dictionary
            del self.contents[item.name]

    def moveItemTo(self, item, destination):
        
        destination.add(item)
        self.remove(item)
        
    def listContents(self):

        text = ""
        for key in self.contents:
            text += key 
            text += " - " 
            text += self.contents[key].description
            text += "\n"
        return text
        
    #itemName keyword is here ******
    def contains(self, itemName):
        """ quick way to check if item is present. """
        # keys() gives us a list of names of items present
        itemNameList = list(self.contents.keys())
        print(itemNameList)
        if itemName in itemNameList:
            return True
        else:
            return False

    
 
       
def main():
     """ test code"""
     pass
if __name__ == "__main__":
    main()