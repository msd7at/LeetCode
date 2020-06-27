# https://leetcode.com/problems/perfect-squares/
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0: return 0
        dp = [0]
        for i in range(1,n+1):
            dp.append(i)
            for j in range(1,i*i):
                if i - j*j < 0:
                    break
                dp[i] = min(dp[i],dp[i-j*j]+1)
        return dp[n]
