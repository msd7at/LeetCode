class Solution:
       def moveZeroes(self, nums: List[int]) -> None:
            l=len(nums)
            s=0
            for i in range(l):
                if nums[i]!=0:
                    nums[i],nums[s]=nums[s],nums[i]
                    s+=1
                    
""" Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Accepted
752,151
Submissions
1,314,424"""
