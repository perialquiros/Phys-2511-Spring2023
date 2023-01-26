#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random as rn
import time as tm

answers = ["Yes.", "No.", "Maybe.", 
           "You\'ll see.", "Don\'t ask me.", "You know the answer."]
answerID = rn.randint(0, 5)
question = input("What is your question? ")
print("\n...Let me think about that.")
tm.sleep(2.5)
print("\nHmm...")
tm.sleep(2.5)
print("\n\"" + question + "\", huh?")
tm.sleep(1.5)
print("\n" + str(answers[answerID]))


# In[21]:





# In[ ]:




