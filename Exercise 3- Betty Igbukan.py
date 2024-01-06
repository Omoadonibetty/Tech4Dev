#!/usr/bin/env python
# coding: utf-8

# In[2]:


def find_maximum_value(lst):
    # Assuming the list contains at least one element
    max_value = lst[0]

    for element in lst:
        if element > max_value:
            max_value = element

    return max_value

input_list = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
result = find_maximum_value(input_list)

print("The maximum value in the list is:", result)


# In[3]:


def calculate_average(lst):
   if not lst:
       # Handle empty list case
        return 0

   total_sum = sum(lst)
   average = total_sum / len(lst)

   return average

input_list = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]
result = calculate_average(input_list)

print("The average value of the list is:", result)


# In[4]:


def print_reverse(lst):
    reversed_list = list(reversed(lst))
    for element in reversed_list:
        print(element, end=' ')

input_list = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
print("Original list:", input_list)
print("List in reverse order:", end=' ')
print_reverse(input_list)


# In[5]:


def compare_lists(list1, list2):
   if len(list1) != len(list2):
       print("False (lists are not the same length)")
       return

   for i in range(len(list1)):
       if list1[i] >= list2[i]:
           print("False")
           return

   print("True")

list1 = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
list2 = [3, 8, 10, 50, 30, 60, 15, 50, 90, 10]

compare_lists(list1, list2)


# In[6]:


def swap_elements(lst, index1, index2):
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        # Swap the elements at index1 and index2
        lst[index1], lst[index2] = lst[index2], lst[index1]
        return True
    else:
        print("Invalid indexes. Please provide valid indexes within the range of the list.")
        return False

input_list = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
print("Original list:", input_list)

index_to_swap1 = 2
index_to_swap2 = 7

if swap_elements(input_list, index_to_swap1, index_to_swap2):
    print(f"List after swapping elements at indexes {index_to_swap1} and {index_to_swap2}:", input_list)


# In[7]:


def concatenate_lists(list1, list2):
    new_list = list1 + list2
    return new_list

list1 = [2, 6, 7, 45, 23]
list2 = [53, 14, 45, 89, 5]

result_list = concatenate_lists(list1, list2)
print("Resulting list:", result_list)


# In[8]:


def last_index_of_value(lst, value):
    if value in lst:
        # If the value is found, find its last index
        last_index = len(lst) - 1 - lst[::-1].index(value)
        return last_index
    else:
        return -1

input_list = [74, 85, 102, 99, 101, 85, 56]
search_value = 85

result = last_index_of_value(input_list, search_value)

if result != -1:
    print(f"The last index of {search_value} in the list is:", result)
else:
    print(f"{search_value} is not found in the list.")


# In[9]:


def calculate_range(lst):
    min_value = min(lst)
    max_value = max(lst)
    value_range = max_value - min_value + 1
    return value_range

input_list = [36, 12, 25, 19, 46, 31, 22]
result = calculate_range(input_list)

print("The range of values in the list is:", result)


# In[10]:


def count_elements_between(lst, min_value, max_value):
   count = 0

   for element in lst:
       if min_value <= element <= max_value:
           count += 1

   return count

input_list = [14, 1, 22, 17, 36, 7, -43, 5]
min_value = 4
max_value = 17

result = count_elements_between(input_list, min_value, max_value)

print(f"The count of elements between {min_value} and {max_value} is:", result)


# In[11]:


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]

result1 = is_sorted(list1)
result2 = is_sorted(list2)

print("Is list1 sorted?", result1)
print("Is list2 sorted?", result2)



# In[ ]:




