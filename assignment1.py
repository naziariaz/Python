#!/usr/bin/env python
# coding: utf-8

# In[1]:


import platform
print(platform.python_version())


# In[2]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[4]:


pi=3.14
r=float(input("enter radius"));

print(str(pi * r**2));


# In[5]:


firstName=input("enter first name:");
lastName=input("enter last Name");
print(str(lastName)+ " " + str(firstName));


# In[7]:


num1=float(input("enter 1st number:"));
num2=float(input("enter 2nd number:"));
print("sum is=" + str(num1+num2) );


# In[10]:


a= '''Twinkle, twinkle,little,star
             How I wonder what you are!
                    Up above the world so high,
                    like a diamond in the sky.
Twinkel,twinkle,liitle,star.'''
print(a);


# In[ ]:




