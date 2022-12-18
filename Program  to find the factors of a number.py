#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Program to find the factors of a number

num = int(input("Enter a number: "))

# To take input from the user
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(i,"is a factor of",num)
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")


#Factors


# In[ ]:




