#!/usr/bin/env python
# coding: utf-8

# Question 3 (5’)
# 
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 
# Example:
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# 
# Output: 7 -> 0 -> 8
# 
# Explanation: 342 + 465 = 807.
# 
# Modify the “solution” class in question3.py, you may design your input to test it.
# 

# In[51]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # add two numbers, return the new list
    def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
        value = ListNode(0)
        index = value # reference value
        # 0 -> next -> next -> None        
        carry = 0 # variable when the 2 digit sums over 10
        # find the sum of the digit of the next node, then move to the next node        
        while l1 or l2 or carry: # while elements still exist in the list or carry           
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, remainder = divmod(val1+val2+carry, 10) # use divmod for sum over 10 and remainder    
                      
            index.next = ListNode(remainder) # next resultant node digit
            index = index.next # move to the next resultant node                      
            
            if l1 and l2: # keep moving to the next node on list 1 and list 2
                l1 = l1.next
                l2 = l2.next
            else:
                None
               
        return value.next # return the next value, starting from 0 node

L1 = ListNode(2,ListNode(4,ListNode(3)))
L2 = ListNode(5,ListNode(6,ListNode(4)))
L3 = Solution.addTwoNumbers(L1,L2)
print(L3.val,(L3.next).val,((L3.next).next).val)

