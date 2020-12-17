#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#python assignment 1


# 1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[22]:


nl=[]
for x in range(2000, 3200):
    if (x%7==0) and  (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


# 2.Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[10]:


firstname = input("Input your First Name : ")
lastname = input("Input your Last Name : ")
print (" " + lastname + " " + firstname)


# 3.Write a Python program to find the volume of a sphere with diameter 12 cm.
# 
#   Formula: V=4/3 * π * r 3

# In[21]:


pi = 3.1415926535897931
d=12
r=d/2
r= 6.0
r3=r*3
V= 4/3*pi* r3
print('The volume of the sphere is: ',V)

