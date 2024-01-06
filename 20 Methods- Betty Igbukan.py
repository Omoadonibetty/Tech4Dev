#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Append
my_list = [2, 4, 8]
my_list.append(12)
print(my_list)


# In[3]:


#2.Extend
list1 = [2, 4, 8]
list2 = [12, 16, 18]
list1.extend(list2)
print(list1)


# In[4]:


#3.Remove
my_list = [2, 4, 8, 12]
my_list.remove(8)
print(my_list)


# In[7]:


#4.Sort
my_list = [2, 1, 4, 1, 5, 9, 2, 7, 6, 5, 9, 3]
my_list.sort()
print(my_list)


# In[8]:


#5.Reverse
my_list = [11, 26, 38, 49]
my_list.reverse()
print(my_list)


# In[10]:


#6.min() and max()
my_list = [32, 10, 40, 15, 51, 97, 20]
min_value = min(my_list)
max_value = max(my_list)
print(min_value, max_value)  


# In[11]:


#7.len():
my_tuple = (5, 6, 7, 8, 9, 10)
length = len(my_tuple)
print(length)


# In[12]:


#8.sum():
my_tuple = (10, 25, 87, 10003)
sum_values = sum(my_tuple)
print(sum_values)  


# In[15]:


#9. enumerate():
my_tuple = ('apple', 'grape', 'banana', 'watermelon', 'orange')
for index, value in enumerate(my_tuple):
    print(index, value)


# In[16]:


#10. repetition:
my_tuple = (1, 9, 16, 26, 80)
repeated_tuple = my_tuple * 4
print(repeated_tuple) 


# In[17]:


#11. slice():
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sliced_tuple = my_tuple[3:7]
print(sliced_tuple)


# In[19]:


#12. clear():
my_dict = {1,  2, 3, 4, 5, 6, 7, 8, 9, 10}
my_dict.clear()
print(my_dict)  


# In[21]:


#13. dict() constructor:
my_dict = dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)
print(my_dict)


# In[23]:


#14. items():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
items = my_dict.items()
print(items)


# In[24]:


#15. update():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_dict.update({'f': 6})
print(my_dict)  


# In[25]:


#16. values():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
vals = my_dict.values()
print(vals)  


# In[26]:


#17. keys():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
keys = my_dict.keys()
print(keys) 


# In[27]:


#18. get():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
value_of_a = my_dict.get('a')
value_of_f = my_dict.get('f')
print(value_of_a)
print(value_of_f)


# In[29]:


#19. pop():
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
popped_value = my_dict.pop('e')
print(popped_value, my_dict)


# In[30]:


#20. . in keyword for membership:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
is_present = 'e' in my_dict
print(is_present)  


# In[ ]:




