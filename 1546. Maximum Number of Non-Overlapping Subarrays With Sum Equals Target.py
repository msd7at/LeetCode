class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d={0:-1}
        s=0
        c=0
        for i in range(len(nums)):
            s=s+nums[i]
            if s-target in d:
                c+=1
                d={}
            d[s]=i
        return c
