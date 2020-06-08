#array edited
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=len(nums)
        for i in range(l):
            nums[nums[i]%l]+=l
        for i in range(l):
            if nums[i] >= l*2:
                return (i)
