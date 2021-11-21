# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        def lot(root,level):
            if not root:
                level-=1
                return None
            if level  == len(ans):
                ans.append([])   
            ans[level].append(root.val)
            level+=1
            lot(root.left,level)
            lot(root.right,level)
        lot(root,0)
        return ans
