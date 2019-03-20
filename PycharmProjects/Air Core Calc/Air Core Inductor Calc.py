#Air Cored Inductor Calculator
import math

def mainMenu():
    print("************Welcome to Air Core Inductor Calculator**************")
    print("")
    print("1. Single layer inductor")
    print("2. Multi layer inductor")
    print("3. Quit")
    print("")
    while True:
        try:
            selection=int(input("Enter choice: "))
            if selection ==1:
                singlelayer()
                break
            elif selection==2:
                multilayer()
                break       
            elif selection==3:
                break
            else:
                print("Invalid choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-3")
    exit
           

def singlelayer():
   print("**** Single Layer ****")
   turns=int(input("Number of turns: "))
   dia=int(input("Diameter of former in mm: "))
   length=int(input("Length of winding in mm: "))
   topline=((dia/10)**2) * turns**2
   bottomline=(4.5*dia + 10*length)
   induct=topline/bottomline
   print("Value in uH: " + str(induct))
   anykey=input("Enter anything to return to main menu")
   mainMenu
    
def multilayer():
   print("**** Multi Layer ****")
   anykey=input("Enter anything to return to main menu")
   mainMenu
    
#the program is initiated, so to speak, here
mainMenu()