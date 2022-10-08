#!/usr/bin/env python
# coding: utf-8

# Question 5 (5’)
# 
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# Open brackets must be closed by the same type of brackets.
# 
# Open brackets must be closed in the correct order.
# 
# Every close bracket has a corresponding open bracket of the same type.

# In[29]:


# Bartley Cai
class Solution:
    def isValid(self, s: str) -> bool:
        # stack, last in first out method
        stack = []
        open_bracket = ["{","(","["]
        for bracket in self:
            if bracket in open_bracket:
                stack.append(bracket) # append the open bracket
                # cannot start with closed bracket
            else:
                if len(stack)<=0: # if the bracket appended on a empty list is a closed bracket
                    return False # return false, cannot pop an empty list
                # pop removes the last list item and returns the value
                last_bracket = stack.pop()
                if bracket == "]" and last_bracket != "[":
                    return False
                if bracket == ")" and last_bracket != "(":
                    return False
                if bracket == "}" and last_bracket != "{":
                    return False
        if len(stack)==0:
            return True
        else:
            return False

p = "[][]{()}"
print(Solution.isValid(p,0))
p="[}]"
print(Solution.isValid(p,0))               


# In[ ]:




