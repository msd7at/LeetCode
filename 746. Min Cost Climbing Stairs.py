class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1=f2=0
        for i in reversed(cost):
            f1,f2=i+min(f1,f2),f1
        return min(f1,f2)
