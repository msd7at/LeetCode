#https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return root
        val=self.helper(root,limit,root.val)
        if val <limit:
            return None
        return root
    def helper(self,root,limit,path):
        if not root.left and not root.right:
            return path
        if root.left:
            leftval=self.helper(root.left,limit,path+root.left.val)
            if leftval<limit:
                root.left=None
        if root.right:
            rightval=self.helper(root.right,limit,path+root.right.val)
            if rightval < limit:
                root.right=None
        if not root.left and not root.right:
            return float('-inf')
        if not root.left:
            return rightval
        if not root.right:
            return leftval
        return max(leftval,rightval)
