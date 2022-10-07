#!/usr/bin/env python
# coding: utf-8

# Question 4 (5’)
# 
# Given a string s, find the length of the longest substring without repeating characters. You can expect the string length is less than 100, and only contains English letters.
# 
# Example 1:
# 
# Input: s = "abcabcbb"
# 
# Output: 3
# 
# Explanation: The answer is "abc", with the length of 3.
# 

# In[101]:


# Bartley Cai
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = []
        substring = []
        for i in self: # O(n)
            if i not in substring:
                substring.append(i)
            else:
                table.append(substring.copy())
                substring.clear()
                substring.append(i)
        
        maxList = max(table, key = len) # O(n)
        #maxList = max(table, key = lambda i: len(i))
        maxLength = len(maxList)
        #maxList=""
        #maxLength=0
        #for i in table:
        #    if len(i) > j:
        #        j = len(i)
        #        k = i
        return maxList, maxLength

string = "Computation & Simulation"
Solution.lengthOfLongestSubstring(string,None)

