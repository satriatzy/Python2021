##########################################
# Learn Fibonacci In Python
# By Satriatzy
##########################################


import os

os.system('Clear')


#########################################
# In this time we learn Fibonacci
# As we know, Fibonacci is the sum of the two previous numbers


num = 8 #-> first, we want to show how many variable want to show in the bash
count = 0 #-> Second, we start with count from zero. the purpose use count for save the numbers of loop while for limit the count so that the count doesn't exceed the number want to print
num1 = 0
num2 = 1


while count < num :
	print(num1)
	last_num = num1 + num2
	num1=num2 #-> its mean a sequence of numbers which is the sum of the two previous numbers so we create variable 
			  #-> firts variable as a new value for num1 and num2 as a new value from result num1 + num2
	num2=last_num
	count += 1 #-> This means that the count value will increase by 1 every loop until the count limit does not exceed many_ numbers (count <many_numbers) 
