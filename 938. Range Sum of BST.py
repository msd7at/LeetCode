# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            if root.val<low:
                return self.rangeSumBST(root.right,low,high)
            elif root.val>high:
                return self.rangeSumBST(root.left,low,high)
            return root.val+self.rangeSumBST(root.left,low,high)+ self.rangeSumBST(root.right,low,high)
        else:
            return 0
        
        
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ar=0
        def dfs(root):
            if  root:
                if L<=root.val <=R:
                    self.ar+=root.val
                if L< root.val:
                    dfs(root.left)
                if root.val<R:
                    dfs(root.right)
        dfs(root)
        return self.ar            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ar=[]
        def preorder(root):
            if not root:
                return
            preorder(root.left)
            self.ar.append(root.val)
            preorder(root.right)
        preorder(root)
        s=0
        for i in self.ar:
            if i>=L and i<=R:
                s+=i
        return s
                
            
