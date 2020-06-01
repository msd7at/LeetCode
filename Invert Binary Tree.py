class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            if root.left or root.right:
                self.invertTree(root.left)
                self.invertTree(root.right)
                root.left,root.right=root.right,root.left
            else:
                return root
        return root
#or 
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
	    if not root:
		    return None

	    root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
	    return root
