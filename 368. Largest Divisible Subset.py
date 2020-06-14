#link:-https://leetcode.com/problems/largest-divisible-subset/
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==0 or n==1:
            return nums
        nums.sort()
        dp=[1]*n
        ma=1
        for i in range(1,n):
            for j in range(i):
                if nums[i]% nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    if ma < dp[i]:
                        ma=dp[i]
        ar=[0]*ma
        prev= 10**9
        for i in range(n-1,-1,-1):
            if dp[i]==ma and (prev%nums[i]==0 or prev==10**9):
                ar[ma-1]=nums[i]
                ma=ma-1
                prev=nums[i]
        return ar
                
                
