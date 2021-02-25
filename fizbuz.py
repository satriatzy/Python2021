########################################
# Learn Fun Code In Python
# By Satriatzy
########################################

import os

os.system('Clear')


###################################################################################################
# We doing something with python like make summary what have we learn before 
# In this case, we create statement when a number its divided 3 or 5 we call that its Fizz or Buzz
# And when a number can divided with num 3 and 5 we call that its Fizzbuzz
####################################################################################################
num = 1 

while ( num <= 100 ):
	if (num % 3 == 0) and (num % 5 == 0):
		print (str(num) + ": FizzBuzz!")
	elif (num % 3 == 0):
		print (str(num) + ": Fizz!")
	elif (num % 5 == 0):
		print (str(num) + ": Buzz!")
	else:
		print (str(num) + '.')
	num += 1