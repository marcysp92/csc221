"""
Created on Wed Aug 18 13:16:30 2021

@author: pattersm4072
"""

# CSC 221
# M1LAB1 - Double a number
# Marceia Patterson
# 8/18/21


entries = [] #temp global container list for entries
results = [] #temp global container list for results

print("This is the Double A Number program.")
def main():
    """Main Loop of Program."""
       
    # TODO: This should loop
    print("1. Enter your choice")
    print("2. Exit")
    choice = int(input("Choose 1 or 2: "))
    
    while True:
        if choice == 1:
            print("Choice 1 selected")
            userInput()
        else:
            print("Exiting program...")
            print("Your entries :", entries)
            print("Your results :", results)
        break
    
    
def userInput():
    num = int(input("Enter a number: "))
    entries.append(num)
    dblNum = dbl(num)
    results.append(dblNum)
    print(num, "doubled is: ", dblNum)
    
    main()

    

def dbl(num):
    """input: one number.
    outpur: the number * 2"""
    result = num * 2
    return result
#Invokes main function
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    