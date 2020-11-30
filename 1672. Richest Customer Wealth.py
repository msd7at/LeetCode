class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=-1000
        for i in accounts:
            m=max(m,sum(i))
        return m
