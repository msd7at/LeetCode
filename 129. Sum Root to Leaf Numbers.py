#link:-https://leetcode.com/problems/sum-root-to-leaf-numbers/

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def ans(root,sum):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                 return sum*10+root.val
            return ans(root.left,sum*10+root.val)+ans(root.right, sum*10+root.val)
        return ans(root,0)
