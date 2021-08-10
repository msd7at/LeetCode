class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        can=None
        for i in nums:
            if c==0:
                can=i
            if can == i:
                c+=1
            else:
                c-=1
        return can
