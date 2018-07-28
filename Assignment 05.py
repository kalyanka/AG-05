
# coding: utf-8

# ## Problem Statement 1
# 
# Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[1]:


def divideByZero():
    try:
        a = 5 / 0
        print("This line wouldn't be printed.")
    except BaseException:
        print("Caught Exception.")
    
divideByZero()


# ## Problem Statement 2
# 
# Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
#  
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
#  
# subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 
#  
# Output should come as below: 
#  
# Americans  play Baseball.
# 
# Americans  play Cricket.
# 
# Americans  watch Baseball.
# 
# Americans  watch Cricket.
# 
# Indians play Baseball.
# 
# Indians play Cricket.
# 
# Indians watch Baseball.
# 
# Indians watch Cricket.

# In[2]:


subjects =  ["Americans", "Indians"]
verbs = ["Play", "watch"]
objects = ["Baseball", "cricket"]

for subject in subjects:
    for verb in verbs:
        for o in objects:
            print(subject + " " + verb + " " + o)

