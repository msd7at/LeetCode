class Solution:
    def __init__(self):
        self.res=0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def k(root,s):
            if root:
                if root.left:
                    k(root.left,s+str(root.left.val))
                if root.right:
                    k(root.right,s+str(root.right.val))
                if root.left is None and root.right is None:
                    self.res+=int(s,2)
        k(root,str(root.val))
        return self.res
