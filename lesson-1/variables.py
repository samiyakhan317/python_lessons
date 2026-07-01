#LESSON 1: INTRODUCTION TO VARIABLES 
''' Variables are containers for storing data values. 
variables means which can change their value. IN python, we don't need to 
declare variables/types before using them. 
A variable name can be of any length and can consist of letters, numbers, and underscores.
But it's a good practice to use meaningful variable names. '''

name= "github" #this is a string type variable 
print(name) #this will print the value of variable name

#similary we can create variables of other types like integer, float, boolean, etc.
age= 20 #this is an integer type variable
height = 5.9 #this is a float type variable
is_student= True #this is a boolean type variable
print(age)
print(height)
print(is_student)

''' In python we can also assign multiple values to multiple variables in one line.'''
x, y, z = 5, 10, 15
print(x)
print(y)
print(z)

#if we want to print the type of variable, we can use the type() function
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
''''str =string , int= integer , float= floating point number , bool= boolean'''
