class Solution:
    def minSwaps(self, s: str) -> int:
        #length
        
        
        def swapa(s,val):
            l=len(s)
            r=0
            for i in range(0,l,2):
                if s[i]!=val:
                    r+=1
            for i in range(1,l,2):
                if s[i]==val:
                    r+=1
            return r//2  
        
        z=s.count("0")
        o=s.count("1")
        
        if abs(z-o)>1:
            return 1-2
        elif z>o:
            ans=swapa(s,"0")
        elif o>z:
            ans=swapa(s,"1")
        else:
            ans= min ( swapa(s,"0"),swapa(s,"1"))
        return ans
