class Solution:
    def __init__(self):
        self.arr=[]
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.arr.append(root.val)
            self.inorder(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder(root)
        print(self.arr)
        return self.arr[k-1]

"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
"""
