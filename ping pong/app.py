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

#Lists
friends=[1,"Kirollos",True,False,[1,"2y 7aga"]]
codezilla =["programming","python"]

# print True
print(friends[2])

#print [1,"2y 7aga"]
print(friends[-1])

#print IndexError: list index out of range
print(friends[-5])

#print ["Kirollos",True]
print(friends[1:3])

#print ["Kirollos",True,False,[1,"2y 7aga"]]
print(friends[1:])

#print "change false" instead of "false"
friends[3]="change false"
print(friends[3])

#extend friends and codezilla together
friends.extend(codezilla)
#print friends with codezilla
print(friends)

#append its role to add iteam at the last position of list
codezilla.append("Bobos")
#print "programming","python","Bobos" 
print(codezilla)

#insert its role insert(position on the list ,"the data that you want to insert")
codezilla.insert(1,"power")
#print ['programming', 'power', 'python', 'Bobos']
print(codezilla)

#remove its role remove any data that exist in list 
codezilla.remove("power")
#print ['programming',  'python', 'Bobos']
print(codezilla)

#clear it role: remove any thing in the list "No parameters"
#codezilla.remove()

#pop its role : pop the index in list  "No parameters"
codezilla.pop()
print(codezilla)
 
 #index for searching its position 
SEARCHING=codezilla.index("programming")
print(SEARCHING)

 #count for counting variables 
COUNTING=codezilla.count("programming")
print(COUNTING)

 #SORT for sort variables alphaphatic"no parameters"
sort=codezilla.count()
print(sort)

 #copy for copying variables "no parameters"
copy=codezilla.copy()
print(copy)

#list of tuples
list_of_tuples = [(2,3),(5,6),(2,6)]
print(list_of_tuples[0][1])

#functions with parameters and no return 
def say_hi(name,age):
    print("hello " +name+ "Your age is " +str(age)) 

#declare the Function 
say_hi("Kirollos",23)   

#functions with parameters and return 
def cube(length_of_edge):
    return length_of_edge^3

print(cube(3))
  
#if conditions with else if and else
is_hungry = False
wants_to_eat = False

if is_hungry and wants_to_eat:
    print("go eat you are hungry or you just want to eat")

elif is_hungry and not wants_to_eat:
    print("eat so you can survive")

elif not is_hungry and wants_to_eat:
    print("do not eat you are not hungry")

else:
    print ("don't eat")

#if condition in function has parameters and no return
def matching_strings(str_1,str_2):
    if str_1 == str_2:
        print("the 2 strings is matching")
    elif str_1 != str_2:
        print("the 2 strings aren't matching")
    

matching_strings("Kirollos","careless")

#dictionaries
convert_month = {
"jan":"january",
"feb":"febraury",
"mar":"march"
}

#print march
print(convert_month["mar"])
#print march
print(convert_month.get("mar"))

#print None
print(convert_month.get("Kirollos"))

#print  2y 7aga 
print(convert_month.get("Kirollos","2y 7aga"))

#dictionaries
convert_month = {
"jan":"january",
"jan":"febraury",
"jan":"march"
}

#print march
print(convert_month["jan"])


#while loop
i = 1

while i<=10:
    print(i)
    i+=1
    if i==6:
        #jump to while loop again so thout 2,3,4,5,7,8,9,10
        continue
else:
    print("the condition isn't true")