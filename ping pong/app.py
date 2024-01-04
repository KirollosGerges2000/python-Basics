#Python basics 
#scripted by:
#Eng/Kirollos Gerges

#variable
age = "34"
num =23
number=-43

#Boolen
is_male=True

#print function
print("welcome\" ")

#print variable 
print(age)

#use function in print function 
print(age.upper().isupper())

#use length function
length=len(age) 

#print length
print(length)

#detect it location as a string 
print(age.index("4")) 

#replace 34 with 323
age.replace("34","323")
print(age)


#mathmatical operations 

#division
print(12/2)

#reminder 
print(12%2)


#print number as a string and string 
print(num) 
print(str(num)+" is the code")

#absolute
print(abs(number))

#power
print(pow(2,3))

#max,min
print(max(3,4)) 

#round convert decimal number to real
print(round(34.4))


#math library 
from math import *

#for floor return it by less = 5
print(floor(5.4))

#for ceil return it by more = 6
print(ceil(5.4))

#Base class for warnings about encodings
EncodingWarning


#square root 
print(sqrt(4))

#inputs
name=input("Enter your name: ")
print("Hello "+name)

#adding 2 num
num1 = input("Enter firist no:")
num2= input("Enter second number:")
result=float(num1)+int(num2)
print(result)

#Building MadLibs
color=input("Enter a color")
plural_noun=input("Enter a plural noun:")
adjective=input("Enter an adjectiv:")

print("Trees are "+color)
print(plural_noun+" are mean")
print ("please keep it "+adjective)