########################################################
# Learn Tupples in Python and what a different with list
# By Satriatzy
#######################################################

import os
os.system('Clear')

#names = ("Kikan", "Syafah", "Syifah")

#print(names[2]) # tupples same thing as list but another different with list 
				# its tupples can't changed once they're create they're immutable 
#Example use tupple


tuple1 = ("Kikan", "Syafah", "Syifah")

# lets we wanna add one list
# this is it the different. We create second variable

tuple2 = ("Aunty",)

# And then, We create variable 3 as a count

tuple3 = tuple1 + tuple2

print(tuple3) # What can happen?
			  # Sure when we run. Bash show 4 item name
			  # Now, we can combination with len
			  # Like This Below
			  # tuple1 = ("Kikan", "Syafah", "Syifah")
			  # tuple2 = ("Aunty",)
			  # print(tuple1[0:2]) 
			  # That Happened it is bash show just print Kikan and Syafah list
			  # What About when we create third variable like this below
			  # tuple3 = tuple1[0:2]
			  # print(tuple3)
			  # Whats can happened ? 