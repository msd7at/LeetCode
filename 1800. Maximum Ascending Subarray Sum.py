class Solution:
    def maxAscendingSum(self, l: List[int]) -> int:
        ms=l[0]
        cs=l[0]
        for i in range(1,len(l)):
            if l[i]<=l[i-1]:
                cs=l[i]
            else:
                cs+=l[i]  
            ms=max(cs,ms)
            # print(ms,i)
        return ms
