# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def findmax(root,ma):
            while root!=None:
                ma=max(ma,root.val)
                root=root.right
            return ma
        
        if root is None:
            return None
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            if root.left!=None and root.right!=None:
                ma=findmax(root.left,-10000000)
                root.val=ma
                root.left=self.deleteNode(root.left,ma)
                return root
            elif root.left!=None:
                return root.left
            elif root.right!=None:
                return root.right
            else:
                return None
        return root
