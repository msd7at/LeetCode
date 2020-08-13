class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[-1]*nums[0]*nums[1]
        b=nums[-1]*nums[-2]*nums[1-4]
        return max(a,b)
