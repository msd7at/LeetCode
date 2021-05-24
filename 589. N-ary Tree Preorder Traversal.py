"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def solve(root,l):
            if root:
                l.append(root.val)
                for c in root.children:
                    solve(c,l)
                
        l=[]
        solve(root,l)
        return l
