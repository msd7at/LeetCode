class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N=bin(N)
        N=N[2:]
        s=""
        for i in N:
            if i=="0":
                s+="1"
            else:
                s+="0"
        # print(s)
        i=0
        l=len(s)
        
        while i<l and s[i]=="0":
            i+=1
        s=s[i:]
        if s=="":
            return 0
        return int(s,2)
