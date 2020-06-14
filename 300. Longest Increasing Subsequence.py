class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1:
            return n
        dp=[1]*n
        ma=1
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<=dp[j] :
                    dp[i]=dp[j]+1
                    ma=max(ma,dp[i])
        return ma        
                
        
