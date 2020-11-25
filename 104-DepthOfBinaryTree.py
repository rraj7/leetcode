""" 104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3. """


#Solution 1: Recursion approach Time Comp = O(N) Space = O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(self, root):
    if root is None:
        return 0 
    else: 
        left_height = self.maxDepth(root.left)
        print()
        right_height = self.maxDepth(root.right)

        return max(left_height, right_height) +1



#Solution2: Iteration

class Solution():
    def maxDepth(self,root):
        stack = []

        if root is not None: 
            stack.append(1, root)

        

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()

            if root is not None: 
                depth = max(depth, current_depth)
                stack.append(current_depth+1,root.left)
                stack.append(current_depth+1, root.right)
            
        return depth 
