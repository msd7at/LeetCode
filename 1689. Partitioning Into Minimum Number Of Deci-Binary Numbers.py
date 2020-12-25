class Solution:
    def minPartitions(self, n: str) -> int:
        l=list(n)
        for i in range(len(l)):
            l[i]=int(l[i])
        return max(l)
