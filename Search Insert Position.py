class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        h=len(nums)-1
        l=0
        if target>nums[h]:
            return h+1
        elif target<nums[0]:
            return 0
        while l<=h:
            mid=l+(h-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                h=mid-1
            else:
                l=mid+1
        if mid>(h+1)//2:
            return mid
        return mid+1
