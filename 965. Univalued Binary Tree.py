# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root :
            return True
        cv=root.val
        if root.left and root.left.val!=cv:
            return False
        if root.right and root.right.val!=cv:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        ov=root.val
        def fin(root):
            if root is None:
                return True
            if root.val!=ov:
                return False
            return fin(root.left) and fin(root.right)
        return fin(root)
                
