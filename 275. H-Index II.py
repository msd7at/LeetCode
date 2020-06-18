class Solution:
    def hIndex(self, cit: List[int]) -> int:
        n=len(cit)
        
        l=0
        r=n-1
        while l<=r:
            m=l+(r-l)//2
            if cit[m]==n-m:
                return n-m
            elif cit[m]> n-m:
                r=m-1
            else:
                l=m+1
        return n-l
