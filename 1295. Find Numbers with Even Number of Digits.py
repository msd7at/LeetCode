class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            c=0
            while i>0:
                c+=1
                i//=10
            if c%2==0:
                s+=1
        return s
