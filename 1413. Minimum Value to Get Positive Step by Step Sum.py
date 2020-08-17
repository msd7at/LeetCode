class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mi=100000000000000
        s=0
        for i in nums:
            s=s+i
            mi=min(mi,s)
        if mi<0:
            mi=-mi
            mi+=1
        else:
            mi=1
        return mi
