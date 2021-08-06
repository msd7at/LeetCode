class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maax=0
        for i in range(1,len(prices)):
            maax += max(prices[i]-prices[i-1],0)
        return maax
