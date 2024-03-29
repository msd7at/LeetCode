class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        ans=0
        s=0
        for i in nums:
            s=s+i
            if s-k in d:
                ans = ans + d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return ans
