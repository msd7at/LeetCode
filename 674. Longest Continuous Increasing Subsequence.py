#  https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        m=1
        c=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
                m=max(m,c)
            else:
                c=1
        return m
                
        
