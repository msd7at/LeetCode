class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s=[0]*101
        for i in nums:
            s[i]+=1
        c=0
        for i in range(101):
            if s[i]==1:
                c+=i
        return c
