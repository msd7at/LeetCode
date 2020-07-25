# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        if h==0:
            return nums[0]
        while l<h:
            mid=(l+h)//2
            if nums[h]==nums[mid]:
                if nums[mid]==nums[l]:
                    l=l+1
                else:
                    h=mid
            elif nums[h]<nums[mid]:
                l=mid+1
            else:
                h=mid
        return nums[l]
                
                
            
                
            
