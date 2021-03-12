class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s)==1:
            return True
        c=s.count("1")
        k=0
        i=0
        while i<len(s)-1:
            j=i
            if s[i]=="1" and s[i+1]=="0":
                k+=1
            while i<len(s)-1 and s[i]=="1" and s[i+1]=="1":
                i+=1
            if j!=i:
                k+=1
            i+=1
        if s[-1]=="1" and s[-2]!="1":
            k+=1
        if k>1:
            return False
        return True
        
