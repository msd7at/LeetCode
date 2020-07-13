class Solution:
    def reverse(self, x: int) -> int:
        s=""
        if x==0 :
            return 0
        elif x>0:
            p=1
        else:
            x=-(x)
            p=-1
        while x>0:
            n=x%10
            x=x//10
            if s=="" and n==0:
                pass
            else:
                s=s+str(n)
        s=int(s)
        if s>2**31 or s<2**-31:
            return 0
        if p==1:
            return s
        else:
            return -s
