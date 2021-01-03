class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], trs: int) -> int:
        l=sorted(boxTypes,key=lambda l:l[1], reverse=True)
        ans=0
        for i in l:
            temp=i[0]
            if trs>=temp:
                ans+=temp*i[1]
                trs-=temp
            else:
                ans+=trs*i[1]
                return ans
        return ans
            
            
