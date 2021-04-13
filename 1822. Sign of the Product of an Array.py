class Solution:
    def arraySign(self, nums: List[int]) -> int:
        z=0
        n=0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                n+=1
        if n%2:
            return -1
        return 1
