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

# In[15]:


# find the first 2 numbers on a list which sum to a desired value
def solution(list, num): 
    a=0 
    b=0
    checked=[]
    for i in list: # iterate over the provided list
        j = 0 # list indexer
        test = list.pop(0)
        # pop(0) will return the value of the first list item and remove it from the list
        # this will reduce the size of the list per iteration
        # as well as avoid re-calculating numbers e.g. 11+7 and 7+11
        while True:
            # I want do do a while loop to test the sum of the iterator to the remaining list items
            if test + list[j] == num:
                a = test
                b = list[j]
                break # if the sum is my desired number, break the while loop
            else: # if not, increase the list indexer by 1
                j+=1
                if j >= (len(list)-1): # if the list indexer becomes larger than the length of the remaining list, break
                    break
                else:
                    continue
    if a==0 and b==0:
        return None # return None for no solution
    else:
        return a, b 
  
numbers = [0, 21, 78, 19, 90, 13] 
print(solution(numbers, 21))
print(solution(numbers, 25))

