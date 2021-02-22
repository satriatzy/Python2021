########################################
# Learn for Loops In Python
# By Satriatzy
########################################

import os 

os.system('Clear')

# For Loops will lets u iterate things. When we have a list so we can iterate through each item
# function items to putt all of the items into can accesible  

#name = "Abba"

#for x in name:
#	print(x) 

# Now We try create list

#names = ["Abba", "Nani", "Bachtiar"]

#for name in names:
#	print(name) # its mean one item per line from the list it will be show in ur bash
				# Different with Dictionaries. In Dictionaries have two things Remember its a key and value
# This Code for Make dictionaries

fav_juice = {
	"Abba": "Banana",
	"Kikan": "Strawberry",
	"Fairah": "Chocolate",
}

for key,value in fav_juice.items(): # Key and Value u can change what ever initial u want
# Example x,y maybe. i use key and value for make it more understand with my learn to and cant make me confus
	print(key + " Love " + value + " Juice ")

