#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Grilled Cheese","Chocolate Chip Cookie","corn","Turkey","Beans","Sugar Cookie"]
# All of the green things inside of "quotes" are STRINGS!
#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1) #Random integer (number)
print(aList[aRandomIndex])
