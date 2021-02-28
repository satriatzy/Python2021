#############################################
# Learn Functions in Python
# By Satriatzy
#############################################

import os

os.system ('Clear')

####################################################################################
# We started learn How we Building own functions or how to create your own functions 
####################################################################################

def nameit(name): #-> its mean we create functions and parameter in parentheses put a fake variable name a placeholder variable like x, y or what we want 
	print ("Hello " + name)

# After that to use functions what we done create before, we called nameit() in the parentheses we put some name 

nameit("Abba") 

# What About if i want use more than one parameter, so i just put def nameit(first_name, lastname):
# After that print ("Hello" + first_name + " " + last_name)
# And we call back function nameit with parentheses and put into parentheses two parameter name 
# nameit("Abba", "Achmad")

# What About Math functions, so for math we change function not nameit but mathit and lets we started

# def mathit(num1, num2):
# 	  return(num1 + num2) -> return its mean whatever outcome of your function is right and this case we're taking num1 and num2 and we're adding them so this can return result
#print(mathit(9, 1)) or we add some variable we call outcome = mathit (9, 1) after that we create print(outcome)
