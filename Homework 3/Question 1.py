#!/usr/bin/env python
# coding: utf-8

# Question 1 (10’)
# 
# Given an array of integers, find two numbers in it such that they can add up to a specific number.
# You may assume there are exactly one solution, you can’t use the same element twice. (Only time-complexity optimized solution gets full grade)
# 
# Example:
# Given [2, 7, 11, 4], Target = 13.
# The answer is 2 and 11.
# 
# Modify the “solution” function in the question1.py.
# (Analyze your time complexity)
# 
# *According to time complexity, the time for the function to run increases with the size of the function input.

# In[35]:


# Bartley Cai
# find the first 2 numbers on a list which sum to a desired value
# concept: use hashing
# use the desired sum and subtract the number
# if the difference is in the hash table, a pair has been found

def solution(numbers, num):    
    a=0
    b=0
    hash_table = []
    for count, i in enumerate(numbers):
        difference = num - numbers[count]
        if difference in hash_table:
            a = difference
            b = i
            break
        hash_table.append(numbers[count])
    if a==0 and b==0:
        return None
    else:
        return a, b
  
numbers = [0, 21, 78, 19, 90, 13] 
print(solution(numbers, 21))
print(solution(numbers, 25))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
print(solution(numbers, 15))
print(solution(numbers, 20))
import random
numbers = random.sample(range(0,50),50)
print(solution(numbers,43))


# In[ ]:


#new_list = numbers.copy() # O(1)
#try:
#    # iterate over the provided list
#    for i in numbers: # O(n)
        # list indexer
#        j = 0 # O(1)
#        test = new_list.pop(0) # O(1)
        # pop(0) will return the value of the first list item and remove it from the list
        # this will reduce the size of the list per iteration
        # as well as avoid re-calculating numbers e.g. 11+7 and 7+11
#        while True:
            # if the list indexer becomes larger than the length of the remaining list, break
#            if j >= len(new_list): # O(1)
#                break # O(1)
            # I want to check the sum of the iterator to the remaining list items
#            if test + new_list[j] == num: # O(1)
#                a = test # O(1)
#                b = new_list[j] # O(1)
#                raise StopIteration # O(1)
#            else: # O(1)
                # if not, increase the list indexer by 1
#                j+=1 # O(n)

#except StopIteration: # O(1)
#    pass # O(1)
#    if a==0 and b==0: # O(1) 
#        return
#    else: # O(1)

