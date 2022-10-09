#!/usr/bin/env python
# coding: utf-8

# Question 7 (10’)
# 
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum. (Note: A leaf is a node with no children.)
# 
# Example: 
# 
# Given the below binary tree and sum = 22,
# 
#           5
#          / \
#         4   8    
#        /   / \
#       11  13  4
#      /  \      \
#     7    2      1
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 

# In[118]:


# Bartley Cai
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        # bad to use sum as a variable. Changed to Sum instead.
        if root is None:
            return False
        # method, check each subtree recursively
        # subtract the desired sum from each node value
        # until a leaf is reached
        Sum -= root.val
        
        # if target sum is 0 and node is leaf then True
        if Sum == 0 and root.left is None and root.right is None:
            return True
        
        # check each left and right subtree recursively
        nodeL = self.hasPathSum(root.left,Sum)
        nodeR = self.hasPathSum(root.right,Sum)
        
        # return left child or right child for recursion to check if Sum is reached 
        return nodeL or nodeR
    
a5=TreeNode(5); a4=TreeNode(4); a8=TreeNode(8); a11=TreeNode(11); a13=TreeNode(13)
a4=TreeNode(4); a7=TreeNode(7); a2=TreeNode(2); a1=TreeNode(1)
a5.left=a4
a5.right=a8
a4.left=a11
a11.left=a7
a11.right=a2
a8.left=a13
a8.right=a4
a4.right=a1
s=Solution()
print(s.hasPathSum(a5, 22))
print(s.hasPathSum(a5, 23))


# In[ ]:




