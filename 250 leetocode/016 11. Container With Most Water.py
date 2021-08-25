class Solution:
    def maxArea(self, he: List[int]) -> int:
        l=0
        h=len(he)-1
        ma=0
        while l<h:
            m=min(he[l],he[h])
            ma=max(ma,m*(h-l))
            if he[l]<he[h]:
                l+=1
            else:
                h-=1
        return ma
