class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d={}
        c=0
        for i in A:
            for j in B:
                s=i+j
                if s not in d:
                    d[s]=0
                d[s]+=1
        for i in C:
            for j in D:
                s=i+j
                if -s in d:
                    c+=d[-s]
        return c
