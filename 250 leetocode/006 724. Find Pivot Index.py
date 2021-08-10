class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        su=sum(nums)
        s=0
        for i in range(len(nums)):
            if su-nums[i]-s == s:
                return i
            s+=nums[i]
        return -1
