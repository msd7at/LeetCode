#https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=0
        if low%2==1 or high%2==1:
            ans+=1
        return ((high-low)//2)+ans
