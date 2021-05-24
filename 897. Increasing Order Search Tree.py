# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        def io(root):
            if not root:
                return
            io(root.left)
            l.append(root.val)
            io(root.right)
        io(root)
        o=l[0]
        node=TreeNode(val=o)
        temp=node
        for i in l[1:]:
            node.right=TreeNode(val=i)
            node=node.right
        return temp
        
