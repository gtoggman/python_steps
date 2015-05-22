# -*- coding: utf-8 -*-
"""
Created on Thu May 14 16:41:26 2015

@author: Gaurav
"""

# This is how to comment. To comment and un-comment text, press Control 1

print "Hello Spyder!!"

a = 1

b = 8

c = float(a)/b # variable c is now a floating type variable

#Importing a package

import math

math.log10



True or False

isinstance("c",float)

#Time for functions

def my_func(x):
    if x is True:
        print 'this is true'
    if x is False:
        print 'this is false'
    else:
        print 'what is this'

my_func(3)

a = 20

def aX2(x='default'): # This has a default value
    global a # This links the global variable into the function
    print x*a
    a = 32 # We can now change the global variable 'a' inside the function
    print a

print aX2(x=a*2) # Forcing the input to equal to a variable


string = 'abcdefghijklmnopqrstuvwxyz'

len(string)

y = 'alphabet'

string + y + ' ' + len(string) # Can't  concatenate int and str

string[-2] # Indexing

string[0] == string[-26] # Strings are immutable. Can't change string using single '='

string.capitalize # Capatalize first letter as opposed to UPPER


k = 45

type(k)

# This is how you can convert variables into other types
str(k)
int(k)
float(k)


# Lists can contain anything including variables

l = [k, 2, 'alpha', 9.0]

print l[2:4]

g = l # g is NOT a copy of l. It is merely pointing to the same place as l
# Changing g will also change l
# To create a copy of the list:

g = list(l)

# Split every element in a string into an individual item in a list
g = list(string)

# Combine every item in a list into a string (requires all items be str)
for i in g:
    if i == g[0]:
        a=i
    if i != g[0]:
        a = a+ i
    print a

cat = "\t Im a \ncat"
print cat # Just a reminder on some text stuff

big_cat = """
Multi line
writing
"""
print big_cat

# Intro to objects


# This would input one customer at a time
class customer:
    acct_id = '001'
    First_Name = 'John'
    Last_Name = 'Doe'
    Product = 'Aspire'
    
#%%    
    
# This allows customers to be input as a list
class defcust:
    
    Version = 'Ver 1.0'    # Same for every object created
    
    def __init__(self,x_1,x_2,x_3,x_4):
        self.acct_id = x_1
        self.first_name = x_2
        self.last_name = x_3
        self.product = x_4

# A function associated to an object is called a 'method'

    def Print(self):
        out = self.Version + '\n' + self.acct_id + '\n\t' + 'Name:\t'+ \
        str(self.first_name + self.last_name) +' \n\t' + self.product
        print out

# Private Data -- Ensures that the only way __NPIPhone can be input is after this check
    
    def NPI(self,Phone):
        dgts = '0123456789'
        
        BadFormat = False
        if type(Phone) != type('asd') or len(Phone) != 10:
            BadFormat = True

        for i in Phone:
            if not i in dgts:
                BadFormat = True             
                
        if BadFormat:
            print 'Phone Number is not a string or not 10 digits long'
            return False
         
        self.__NPIPhone = Phone # This is a private variable that can't be accessed outside this object
        
        return True        
        
    def getNPI(self):
        return self.__NPIPhone
    
#%%

# Dividing my code into blocks!

# Calls __init__ function in class 'defcust'

cust1 = defcust('002','Mary','Jane','.') # All items in object must be populated?
cust2 = defcust('003','Mitch','Conner','World')

# Press Shift Enter to execute code & move to next block without switching out of Editor

# Adding Private info

cust1.NPI('41677383867') # Incorrect Phone Number
cust2.NPI('4163338888')


#%%

print cust1.acct_id
print cust2.Version

cust2.Print() # Calls the method 'Print' in class 'defcust'

cust1.getNPI() # Calls function that returns Private info

#%%

# Control+i to learn about 'dir'
dir(cust1)
# Gives list of variables and all methods we defined

#%%

# Testing loops

y = '2123445'
z = '12'


for i in y:
    if not i in z:
        print i

#%%

# Inheritance

class stmt(defcust): # class 'stmt' has all the properties of 'defcust'

    Type = 'Statement'
    
    def __init__(self,x_1,x_2=None,x_3=None,x_4='No Product',stmt=None,finchg=None,phone=None):
        
        defcust.__init__(self,x_1,x_2,x_3,x_4)
        
        self.stmt_no = stmt
        self.fc = finchg
        
        if phone != None:
            self.NPI(phone)
#%%

stmt3 = stmt('004','Alla','Smith',stmt='3',phone='8887864535')     
            
#%%

import pandas as pd

pd.


#%%



