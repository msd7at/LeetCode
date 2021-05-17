# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        d={}
        
        def lot(root,i):
            if not root:
                return 
            if not root.left  and not root.right:
                if i not in d:
                    d[i]=[]
                d[i].append(root.val)
                return
            lot(root.left,i+1)
            lot(root.right,i+1)
            
        lot(root,0)
        
        # print(d)
        
        
        return sum(d[max(d.keys())])
                
            
        
