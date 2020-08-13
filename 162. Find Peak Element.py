class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]>nums[mid+1]:
                h=mid
            else:
                l=mid+1
        return l
            
