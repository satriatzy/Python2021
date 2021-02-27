##################################################################
# Learn With Python
# By Satriatzy
##################################################################


import os

os.system ('Clear')

##########################################################################################
# We started to create more function with fizbuz to make summary what we have learn before
# In this time we want create function counter where its count how many fizz, buzz and fizzbuzz have

# First Step

num = 1
fizzcount = 0
buzzcount = 0
fizzbuzzcount = 0

while (num <= 10000):
	if (num % 9 == 0) and (num % 10 == 0):
		print(str(num) + ": FizzBuzz!")
		fizzbuzzcount += 1

	elif (num % 9 == 0):
		print(str(num) + ": Fizz!")
		fizzcount += 1

	elif (num % 10 == 0):
		print(str(num) + ": Buzz!")
		buzzcount += 1

	else:
		print(str(num) + '.')
	
	num += 1

print ("____________________")
print ("Fizz\tBuzz\tFizzBuzz")
print (str("{:,}".format(fizzcount)) + "\t" + str("{:,}".format(buzzcount)) + "\t" + str("{:,}".format(fizzbuzzcount)))

