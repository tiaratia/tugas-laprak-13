#!/usr/bin/env python
# coding: utf-8

# In[4]:


# mencari faktorial 

def faktorial(n):
    if n == 1:
        return n
    else:
        return n * faktorial (n-1)
print (faktorial (5))
    


# In[7]:


def faktorialwhile (n):
    hasil = 1
    while n > 0:
        hasil = hasil * n
        n = n-1
    return hasil
print (faktorialwhile (4))     


# In[11]:


def fibonacci (n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci (n-2)
print(fibonacci(10))
    


# In[12]:


def factorial(x):
    if x == 1: # ini adalah base case
        return 1

    else: # ini adalah  recursive case
        return(x * factorial(x-1))

print(factorial(4))


# In[ ]:




