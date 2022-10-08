#!/usr/bin/env python
# coding: utf-8

# Question 8 (10’)
# 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 
# Example 1:
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# Example 2:
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# Constraints:
# 
# 1 <= s.length, t.length <= 5 * 104
# 
# s and t consist of lowercase English letters.

# In[7]:


# Bartley Cai
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = list(s)
        list2 = list(t)
        # if the length of the two strings are not equal, then False
        if len(list1)!=len(list2): 
            return False
        for i, j in zip(list1,list2):
            # if i in string 1 or j in string 2 are not in each other, then False
            if i not in list2 or j not in list1:
                return False
            else:
                return True

s="anagram"
t="nagaram"
S=Solution()
print(S.isAnagram(s,t))
s="car"
t="rat"
print(S.isAnagram(s,t))


# In[ ]:




