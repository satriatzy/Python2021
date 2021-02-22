#############################
# Learn Dictionaries in python
# By Satriatzy
#############################

import os
os.system('Clear')

# In this lecture, we learn function dictionaries in python
# Let we started

favorite_drink = {
	"Abba": "Latte",
	"Anita": "Chocolate",
	"Tria": "Blueberry"
}

#print(favorite_drink["Abba"]) # Now how when we want chose a specific item in dictionaries ?
					  # so we create like this below
					  # print(favorite_drink["Abba"]) its mean we just chose key and the bash will show the value
					  # in this case i chose ["Abba"] as the key and its absolutely the bash print latte as a value 
# Now How we want something diffrent like we want to delete some item in dictionaries
# So this is the code

# del favorite_drink["Abba"]

# print(favorite_drink)

# How about add more item in the dictionaries use function update
# So let start with 
#favorite_drink.update({"Bactiar": "Banana"})

#print(favorite_drink)

# Now How about we want to change value in the key Abba as Redvelvet
# This is the code
favorite_drink ["Abba"] = "Redvelvet"

print(favorite_drink) # what can happend when i print like this below

# print(favorite_drink[Abba])
# sure, the bash show Redvelvet as a value from key Abba