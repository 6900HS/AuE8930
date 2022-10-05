#!/usr/bin/env python
# coding: utf-8

# Question 2 (10’)
# 
# Given a binary tree, find the max depth of it. Modify the “solution” function in the question2.py
# (Analyze your time complexity, and only time-complexity optimized solution gets full grade)

# In[40]:


# Bartley Cai
class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
# this checks the depth of a tree from the specified node
# any parent nodes are not considered
# therefore, to obtain max depth, the "ancestor" node must be known
    if root is None: 
        return 0
    if root is 
    else:
        # check each subtree depth
        # recursion
        right_depth = solution(root.right)
        left_depth = solution(root.left)
        # recursion indicates O(n) complexity
        if right_depth > left_depth:
            return right_depth+1
        else:
            return left_depth+1

    #return depth

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
print(solution(a3))

