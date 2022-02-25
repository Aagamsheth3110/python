# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 17:08:07 2022

@author: AAGAM
"""


                    # ASSIGNMENT 1.1(1) : USE ALL OPERATORS
                    
 
#1.0 ARITHMETIC OPERATORS


a = 30
b = 10

a + b   #addition

a - b   #substraction

a * b   #multiplication

a / b   #division

a ** b  #power or exponentiation

a % b   #modulus or remainder

a // b  #floor division


# 1.1 ASSIGNMENT OPERATORS

x = 10  #assign

y = 20

y+= 2   #same as y = y + 2                

x-=2    #same as x = x - 2

y*=5    #same as y = y * 5

x/=4   #same as  x = x / 4                

x%=2    #same as x = x % 2

y//=3    #same as y = y // 3

y**=2    #same as y = y ** 2

y &= 4   #same as y = y & 4 

y |= 3   #same as y = y | 3

y ^= 2   #same as y = y ^ 2

y >>= 5   #same as y = y >> 5

y <<= 6   #same as y = y >> 6



#1.2 LOGICAL OPERATORS

s = 10 
s > 5 and s < 23 #and operators

s < 7 or s < 12 #or operators

(not(s > 5 and s < 23)) #not operators


#1.3 COMPARISON OPERATORS

p = 40
q = 40

p == q   #equal

p != 1  #not equal

p > q   #greater than 

p < q  #less than

p >= q  #greater than or equal to

p <= q  #less than or equal to


#1.4 IDENTITY OPERATORS

x = [10,30,60]
y = [10,30,60]
z = x


x is z    # IF BOTH VARIABLES ARE SAME OBJECT 

x is y    # IF BOTH VARIABLES ARE SAME OBJECT BUT THEY HAVE NOT SAME LOCATION

x is not z # IF BOTH VARIABLES ARE NOT THE SAME OBJECT


#1.5 MEMBERSHIP OPERATORS

h= [10,20,50,90]

20 in h   #if value in sequence then true otherwise false
 
15 not in h  #if value is not in sequence then true otherwise false
50 not in h


#BITWISE OPERATORS  (and,or,not,xor,xnor)

m = 1001
n = 1010

m and n  #and opearators 

m or n 

not m

                  # ASSIGNMENT 1.1(2) : WRITE AN ALGORITHM 
                  
      # write an algorithm for (10,1,8,3,6,5,4,7,x,y)

#step 1 : Entry

#step 2 : Import the Random module.

#step 3 : Read variable 'random'

#step 4 : Store the random number from 1 to 10 by using the random module in the variable 'random'.

#step 5 : Print the value in 'random' which is stored in random variable.

#step 6 : Exit            
                  
                      # OR 2ND OPTION 
                      
#Step 1: Start

#Step 2: Initialize variable number as integer

#   Like number (n) = 1

#Step 3: Read and print the value of number

#Step 4: Repeat the step 3 until number < 10 and when condition is satisfied then exit loop

# 4.1: number = number (n) + 1

#Step 5: Stop
                 
                  
                  
                  
                 
          # ASSIGNMENT 1.2(1) : USE ALL LOGICAL OPERATORS IN IF CONDITION
                
                
#and operators in if caondition                
x = int(input("enter value of x :"))
y = int(input("enter value of y :"))

if x > 20 and y < 25:
    print("this value is true")
else:
    print("this value is false")


#or operators in if condition

a = int(input("enter value of a:"))

  
if  (a%7 == 0 or a%10 == 0):
    print(a,"is divisible by either 7 or 10")
else:
    print(a,"is not divisible by either 7 or 10")


#not operators in if condition

z = "buy a new phone"
if not z :
    print("not buy simcard")
else:
    print("buy simcard")
    

                   
               
                  # ASSIGNMENT 1.2(2) : BUILD SIMPLE CALCULATOR 
                  
# To make a simple calculator

# take inputs
value1= int(input("Enter first number: "))
value2= int(input("Enter second number: "))

# choise operation
print("Operation: +, -, *, /, %, //, **")
choose = input("Select operations: ")

# check operations and display result
# add(+) two numbers
if choose == "+":
    print(value1, "+", value2, "=", value1 + value2)

# subtract(-) two numbers
elif choose == "-":
    print(value1, "-", value2, "=", value1 - value2)

# multiplies(*) two numbers
elif choose == "*":
    print(value1, "*", value2, "=", value1 * value2)

# divides(/) two numbers
elif choose == "/":
    print(value1, "/", value2, "=", value1 / value2)

# modulo(%) two numbers
elif choose == "%":
    print(value1, "%", value2, "=", value1 % value2)

# floor division(//) two numbers
elif choose == "//":
    print(value1, "//", value2, "=", value1 // value2)

# power(**) two numbers
elif choose == "**":
    print(value1, "**", value2, "=", value1 ** value2)
    
    
else:
    print("error : please choose correct opearations")
        
    
    
    
             # ASSIGNMENT 2.1(1) : CHANGE VALUE IN LIST  & DICTIONARY
                       
            
#change value in list 

list=[ 20, 22, 24, 26, 28, 30, 32, 35 ] 

print("original list ") 
print(list) 

#changing the first value 
list[0] = 53

#changing the second value 
list[1] = 55

#changing the last element 
list[ -1] = 57

#changing the last second element 
list[ -2] = 60

print("\nNew list") 
print(list)



#change value in dictionary

dictionary = {1:"Aagam" , 2:"Shashank" , 3:"Kiyara" , 4:"Salman" , 5:"jackson"}

dictionary[3] ="Shaili"
dictionary["Tiger"] = 5

dictionary.update({2:"Anita", 4:"Katrina"})

print(dictionary)





        # ASSIGNMENT 2.1(2) : Methods of list,dictionary,string
                    

#LIST METHOD

bigbull = ["Ratan tata", "Mukesh ambani", "Amitabh bachhan", "Harshad mehta", "Harshad mehta"]

#1(append)

bigbull.append("Gautam adani")
print(bigbull)

#2(copy)

bear= bigbull.copy()
print(bear)

#3(count)

bear = bigbull.count("Harshad mehta")
print(bear)

#4(extend)

stock = ["Tata power", "Reliance", "polo", "Adani power"]
stock.extend(bigbull)
print(stock)

#5(index)

bear= bigbull.index("Mukesh ambani")
print(bear)

#6(insert)

bigbull.insert(2,"Anil ambani")
print(bigbull)

#7(pop)

bigbull.pop(2)
print(bigbull)

#8(remove)

bigbull.remove("Harshad mehta")
print(bigbull)

#9(reverse)

bigbull.reverse()
print(bigbull)

#10(sort)

bigbull.sort()
print(bigbull)

#11(clear)

bigbull.clear()
print(bigbull)


#DICTIONARY METHOD

hotel = {1:"oyo", 2:"taj", 3:"hyaat", 4:"heritage"}

#1 (copy)

hotel.copy()
print(hotel)

#2 (formkeys)

x = ('hour :', 'miniute :', 'second :')
y = 10
dictionary = dict.fromkeys(x, y)
print(dictionary)

#3 (get)

x = hotel.get(2)
print(x)

#4 (items)

x = hotel.items()
print(x)

#5 (keys)

x = hotel.keys()
print(x)

#6 (pop)

hotel.pop(3)
print(hotel)

#7 (popitem)

hotel.popitem()
print(hotel)

#8 (setdefault)

x = hotel.setdefault(1)
print(x)

#9 (update)

hotel.update ({5: "starbucks"})
print(hotel)

#10 (value)

x = hotel.values()
print(x)

#11 (clear)

hotel.clear()
print(hotel)


#STRING METHOD 

#1 (capitalize)
#Converts the ONLY first character to upper case

str1 = "hey, aagam how are you ? "
value_store = str1.capitalize()           
print (value_store)

#2 (caefold)
 #Converts WHOLE string into lower case

str1 = "Hey, AAGAM Welcome   ? "
value_store = str1.casefold()           
print (value_store) 

#3 (center)
# centered string (in arguments shows spacing to strat)
  
str1 = "AAGAM"
value_store = str1.center(20)         
print(value_store)

#4 (count)
#Returns the number of times a specified value occurs in a string

str1 = "Hey, aagam Welcome ; hey, aagam how are you  ? "
value_store = str1.count("aagam")           
print (value_store) 

#5 (encode)
#Returns an encoded version of the string

txt = "My name is Ståle"
x = txt.encode()
print(x)

#6 (endswith)
#Returns true if the string ends with the specified value

str1 = "hey, aagam how are you ? "
value_store = str1.endswith(" ? ")           
print (value_store)

#7 (expandtabs)
#Sets the tab size of the string

str1 = " A\tA\tG\tA\tM\t. " 
value_store = str1.expandtabs(4)           
print (value_store)

#8 (find)
#Searches the string for a specified value and returns the position of where it was found

str1 = "hey, aagam how are you ? "
value_store = str1.find("aagam")           
print (value_store)


#9 (format)
#Formats specified values in a string

str1= "We have {:d} fivestar."
x = str1.format(0b1110)
print(x)

#10 (index)
#Searches the string for a specified value and returns the position of where it was found

str1 = "hey, aagam how are you ? "
value_store = str1.index("you")           #same as find 
print (value_store)

#11 (isalnum)
#Returns True if all characters in the string are alphanumeric

str1 = "aagam12"        #either num or letter
value_store = str1.isalnum() 
print (value_store)


#12 (isalpha)
#Returns True if all characters in the string are in the alphabet

str1 = "aagam1"        # only letter
value_store = str1.isalpha() 
print (value_store)

#13 (isdecimal)
#Returns True if all characters in the string are decimals

str1 = "\u0030" #unicode for 0       # decimal no
value_store = str1.isdecimal() 
print (value_store)

#14 (isdigit)
#Returns True if all characters in the string are digits

str1 = "9328121475"        # only digit
value_store = str1.isdigit() 
print (value_store)


#15 (isidentifier)
#Returns True if the string is an identifier

str1 = "Aagam"        # alphanumeric letters (a-z) and (0-9), or underscores (_) . A valid identifier cannot start with a number, or contain any spaces.
value_store = str1.isalpha() 
print (value_store)

#16 (islower)
#Returns True if all characters in the string are lower case

str1 = "Hey How Are You"        
value_store = str1.islower() 
print (value_store)

#17 (isnumeric)
#Returns True if all characters in the string are numeric

str1 = "123"        
value_store = str1.isnumeric() 
print (value_store)

#18 (isprintable)
#Returns True if all characters in the string are printable

str1 = "Hey How Are You #12 ?"        
value_store = str1.isprintable() 
print (value_store)


#19 (isspace)
#Returns True if all characters in the string are whitespaces

str1 = "  "        
value_store = str1.isspace() 
print (value_store)


#20 (istitle)
#Returns True if the string follows the rules of a title

str1 = "Hey How Are You"        
value_store = str1.istitle() 
print (value_store)


#21 (isupper)
#Returns True if all characters in the string are upper case

str1 = "Hey How Are You"        
value_store = str1.isupper() 
print (value_store)


#22 (join)
#Joins the elements of an iterable to the end of the string

list1 = ["Sheth", "Aagam", "B."]
x = "_".join(list1)
print(x)


#23 (ljust)
#Returns a left justified version of the string

str1 = "Mango"
x = str1.ljust(10)
print(x, "is my favorite fruit.")

#24 (lower)
#Converts a string into lower case

str1 = "Hey How Are You"        
value_store = str1.lower() 
print (value_store)

#25 (lstrip)
#Returns a left trim version of the string

str1 = " Mango        "
x = str1.lstrip()
print("all of the fruits are good but", x , "is my favorite")


#26 (maketrans)
#Returns a translation table to be used in translations

str1 = "Hello Aagam :"
value_store = str1.maketrans("m", "u")
print(str1.translate(value_store))

#27 (partition)
#Returns a tuple where the string is parted into three parts

str1 = "I love mango and watermelon"
x = str1.partition("mango")
print(x)

#28 (replace)
#Returns a string where a specified value is replaced with a specified value

str1 = "I like ford car"
y = str1.replace("ford", "Tata")
print(y)

#29 (rfind)
#Searches the string for a specified value and returns the last position of where it was found

str1 = "I like  ford car"
y = str1.rfind("ford")
print(y)

#30 (rindex)
#Searches the string for a specified value and returns the last position of where it was found

str1 = "I like ford car"
y = str1.rindex("car")
print(y)

#31 (rjust)
#Returns a right justified version of the string

str1 = "I like  ford car"
y = str1.rjust(50)
print(y)

#32 (rpartition)
#Returns a tuple where the string is parted into three parts

str1 = "I like  ford car"
y = str1.rpartition("ford")
print(y)

#32 (rsplit)
#Splits the string at the specified separator, and returns a list

str1 = "I like  ford car"
y = str1.rsplit(" ? ")
print(y)

#33 (rstrip)
#Returns a right trim version of the string

str1 = " Mango   "
x = str1.rstrip()
print("all of the fruits are good but", x , "is my favorite")

#34 (splitlines)
#Splits the string at line breaks and returns a list

str1 = "hello welcome welcome\nhow are you"
x = str1.splitlines()
print(x)


#35 (startswith)
#Returns true if the string starts with the specified value

str1 = "hello welcome, how are you"
x = str1.startswith("welcome")
print(x)

#36 (strip)
#Returns a trimmed version of the string

txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#37 (swapcase)
#Swaps cases, lower case becomes upper case and vice versa

str1 = "Hello My Name Is AAGAM"
x = str1.swapcase()
print(x)

#38 (title)
#Converts the first character of each word to upper case

str1 = "hello , My name is aagam"
x = str1.title()
print(x)

#39 (translate)
#Returns a translated string


#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello sasam!"
print(txt.translate(mydict))


#40 (upper)
#Converts a string into upper case

str1 = "Hello my name is aagam"
value_store = str1.upper()
print(value_store)


#41 (zfill)
#Fills the string with a specified number of 0 values at the beginning

values = "500"
x = values.zfill(5)
print(x)