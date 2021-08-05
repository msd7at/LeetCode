class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=10**6
        maxp=0
        for i in prices:
            if i < minp:
                minp = i
            elif i - minp > maxp:
                maxp = i- minp 
        return maxp
