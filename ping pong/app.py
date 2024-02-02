#Python basics 
#scripted by:
#Eng/Kirollos Gerges

#variable
age = "34"
num =23
number=-43

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

    #for loops
    names=["kirollos","Bishoy"]
    for letter in "code":
        #print c
        #o
        #d
        #e
        print(letter)
    for name in names:
        #print kirollos
        #      Bishoy
        print(name)

    for x in range(len(names)):
        #print 0
        #       1
        print(x)
        #print "kirollos","Bishoy"
        print(name(x))

#Exponent function
#print 8
print(2**3)
def power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
#print 8
print(power(2,3))

#Nested Loops [2D List]
no_list = [
 [1,2,3],
 [4,5,6],
 [7,8,9],    
[0]
]

#Print [1,2,3],[4,5,6],[7,8,9],[0]
print(no_list)
#print first row [1,2,3]
print(no_list[1])
#print 8 
print(no_list[2][1])

for x in no_list:
    #print  [1,2,3],
 #          [4,5,6],
 #          [7,8,9],    
#           [0]
    print(x)

for ROW in no_list:
    for column in ROW:
          '''
          #comments
          print 1
                 2
                 3
              4
                5
                6
              7
               8
                 9    
              0
'''
    print(column)

#prevent user from Run time error
    # by using try, except 
try:
    result=32/0
    value=int(input("Enter value:"))
    print(value)
except ZeroDivisionError as error:
    print(error)
except ValueError as value_error:
    print(value_error)
print("success")

#Reading Files 
#open this file in read mode 
FILE=open("FILE.txt","r")
#open this file in write mode 
open("FILE.txt","w")
#open this file in append mode to 
#insert data but not delete data
open("FILE.txt","a")
#open this file in read,write mode 
open("FILE.txt","r+")
#print true in read while false in write 
print(FILE.readable())
#print Kirollos Gerges >>>>>>> Embedded C enginnering 
print(FILE.read())
#print Kirollos Gerges >>>>>>>
print(FILE.readline())
#print Embedded C enginnering 
print(FILE.readline())
#print "Kirollos Gerges >>>>>>>\n" 
#"Embedded C enginnering\n" 
print(FILE.readlines())
#print Embedded C enginnering 
print(FILE.readlines()[1])
FILE.close()

#writing files 
 #open this file in append mode 
files=open("FILE.txt","a")
#file will be
#Kirollos Gerges >>>>>>>
 #Embedded C enginnering 
#Good Enginner
files.write("\nGood Enginner")
list_of_phrases=["\n firist","\nsecond"]
#will write this lines
files.writelines(list_of_phrases);
files.close()

#Libraries
#using for bytes and integers
import random
#roll_dice will print number 
#from 0 to 9 randomly
print(random.roll_dice(9))
#for more modules visit
#https://docs.python.org/3/py-modindex.html
#Encodindg library by asciis
import base64
base64.a85decode
#for install python.docx visit
#https://python-docx.readthedocs.io/en/latest/

#python classes and objects
from Employee import Employee
from Employee import student

employee1=Employee("Kirollos",24,"self learning",False)
employee2=Employee("Gerges",57,"IT",True)

student1 =student("Bishoy",22,3.8)

#print 24 57
print(employee1.age,employee2.age)
#print Bishoy 22 3.8 
print(student1.name,student1.age,student1.gpa)

#class function
#print false
print(employee1.is_manager())
#print true
print(employee2.is_manager())

#class inheritence Tut 33
from Doctor import Doctor
from Family_doctor import Family_doctor

doctor1=Doctor()
doctor2=Family_doctor()

#print I work with families
doctor2.what_specialization()

#print I studied 7 years
doctor1.studied_years()
#print I work in a hospital
doctor1.works_where()

#python Pong Game 
#in PingPong File


#object oriented programming "OOP"
#1)Encapsulation "independent function"
#2)polymorphism
#3)Abstraction
#4)Inheritence

#object is an instance of class.
#class is  an templete of object. 
#"contains Functions by getters"return"
# and setters methods"No return "

#what is encapsulation? كبسولة 
#as Blackbox that help us in testing

#Abstraction
#Input and outputs according to user.
#According to interface and Implementation.
#by using class method.

#Always use inheritence by using base_classor super class

#polymorphism متعدد الأشكال"use single action with multiple 
#resources"
#by method overriding + overloading(multiple
#functions"methods" in the same class with 
#different parameters)

#Practical
#get data type but must the same object
x=type(sum)
#get id of the sum
x1=id(sum)

#for private and public classes

#private class
class Employee:
    def __init__(self,name,age,depertment,is_manager):
        self.__name=name
        self.__age=age
        self.__depertment=depertment
        self.__manager=is_manager

#public class
class Employee:
    def __init__(self,name,age,depertment,is_manager):
        self.name=name
        self.age=age
        self.depertment=depertment
        self.manager=is_manager

from datetime import date
#Class method to change the behavior of classes
@classmethod
def initFromBirthYear(cls,name,birthYear):
    return cls(name,date.today().year - birthYear)


student33=student.initFromBirthYear("Kirollos",2000)
#print my name is Kirollos and my age is 24.
student33.describe() 

#print dirctory of student33 __init__ 
#__dir__  __doc__
print(dir(student33))


#static methods "Helper method or utality"
@staticmethod
def add22(x):
    return x+10

#print True
print(isinstance(student33,student))


#Dunder Functions














