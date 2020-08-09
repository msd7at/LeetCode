class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        da=[]
        if s==t:
            return True
        ns=len(s)
        nt=len(t)
        if nt!=ns:
            return False
        for i in range(ns):
            d=ord(t[i])-ord(s[i])
            if d<0:
                d=26+d
            da.append(d)
        m={}
        for i in da:
            if i==0:
                continue
            if i in m:
                m[i]+=26
            else:
                m[i]=i
            if m[i] > k:
                return False
        return True
