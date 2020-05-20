class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root:
            l=self.maxDepth(root.left)
            r=self.maxDepth(root.right)
            if r>l:
                return r+1
            else:
                return l+1
  
   """
   Given a binary tree, find its maximum depth.

he maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Givn binary tree [3,9,20,null,null,15,7], 
"""
