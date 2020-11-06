class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        beg=0
        end=max(nums)+1
        while beg+1 <end:
            mid=(beg+end)//2
            if sum(ceil(num/mid) for num in nums) <= threshold:
                end=mid
            else:
                beg=mid
        return end
