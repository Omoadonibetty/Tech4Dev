#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_pattern(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("+----+")
        else:
            print("\\    /")
            print("/    \\")
rows = 6 

print_pattern(rows)


# In[3]:


rows = 5
columns = 10

for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print() 


# In[4]:


for i in range(1, 7):
    print(i)


# In[8]:


for num in range(2, 14, 2):
    print(num)


# In[9]:


for num in range(4, 80, 15):
    print(num)


# In[12]:


for num in range(30, -21, -10):
    print(num)


# In[14]:


for num in range(-7, 13, 4):
    print(num)


# In[20]:


for num in range(97, 80, -3):
    print(num)


# In[23]:


for num in range(-4, 87, 18):
    print(num)


# In[24]:


class NumberTriangle:
    def __init__(self, num_lines):
        self.num_lines = num_lines

    def print_triangle(self):
        for i in range(1, self.num_lines + 1):
            line = str(i) * i
            print(line)

NUM_LINES = 7

triangle = NumberTriangle(NUM_LINES)

triangle.print_triangle()


# In[25]:


def pay(salary, hours_worked):
    regular_hours = min(hours_worked, 8)
    overtime_hours = max(hours_worked - 8, 0)

    regular_pay = salary * regular_hours
    overtime_pay = 1.5 * salary * overtime_hours

    total_pay = regular_pay + overtime_pay
    return total_pay

result = pay(5.50, 6)
print(result)  

result = pay(4.00, 11)
print(result)  


# In[26]:


import math

def area(radius):
    return math.pi * radius ** 2

radius = 2.0
result = area(radius)
print(result)


# In[27]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)


# In[28]:


low = int(input("low? "))
high = int(input("high? "))
sum = 0

for i in range(low, high):
    sum += i

print("sum =", sum)


# In[29]:


sum = 0

while True:
    num = int(input("Enter a number (type 0 to stop): "))
    
    if num == 0:
        break

    sum += num

print("Sum of the numbers:", sum)


# In[31]:


sum = 0

while True:
    num = int(input("Enter a number (type -1 to stop): "))
    
    if num == -1:
        break

    sum += num

print("Sum of the numbers:", sum)


# In[32]:


def repl(s, repetitions):
    if repetitions <= 0:
        return ""
    else:
        return s * repetitions

result = repl("hello", 3)
print(result)  


# In[33]:


def printRange(start, end):
    if start < end:
        for i in range(start, end + 1):
            print(i, end=" ")
    elif start > end:
        for i in range(start, end - 1, -1):
            print(i, end=" ")
    else:
        print(start)

printRange(2, 7)
print()

printRange(19, 11)
print()

printRange(5, 5)
print()


# In[34]:


def smallestLargest():
    count = int(input("How many numbers do you intend to enter? "))
    
    if count <= 0:
        print("Invalid input. Please enter a number greater than 0.")
        return

    smallest = float('inf')  
    largest = float('-inf')  

    for i in range(1, count + 1):
        number = float(input(f"Number {i}: "))
        smallest = min(smallest, number)
        largest = max(largest, number)

    print(f"Smallest = {smallest}")
    print(f"Largest = {largest}")
smallestLargest()


# In[35]:


def printAverage():
    total = 0
    count = 0

    while True:
        num = float(input("Enter a number: "))
        
        if num < 0:
            break  
        
        total += num
        count += 1

    if count > 0:
        average = total / count
        print(f"Average was {average:.1f}")
    else:
        print("No nonnegative numbers entered.")

printAverage()


# In[36]:


def numUnique(a, b, c):
    unique_set = set([a, b, c])
    return len(unique_set)

result = numUnique(18, 3, 4)
print(result) 

result = numUnique(6, 7, 6)
print(result) 


# In[37]:


import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls():
    tries = 0
    while True:
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print(f"{dice1} + {dice2} = {total}")

        tries += 1

        if total == 7:
            print(f"You won after {tries} tries!")
            break

simulate_dice_rolls()


# In[ ]:




