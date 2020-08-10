class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sd={}
        for i in s:
            if i not in sd:
                sd[i]=1
            else:
                sd[i]+=1
        dd={}
        for i in t:
            if i not in dd:
                dd[i]=1
            else:
                dd[i]+=1
        m1=0
        for i in dd:
            if i not in sd:
                m1+=dd[i]
            else:
                if dd[i]>sd[i]:
                    m1=m1+dd[i]-sd[i]
        return m1
                
