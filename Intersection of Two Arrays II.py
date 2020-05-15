class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        if len(nums1)<len(nums2):
            l1=nums1
            l2=nums2
        else:
            l1=nums2
            l2=nums1
        for i in l1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=[]
        for i in l2:
            if i in d and d[i]>0:
                s.append(i)
                d[i]=d[i]-1
        return s
  """
  Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?"""
