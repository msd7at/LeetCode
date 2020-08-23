class Solution:
    def thousandSeparator(self, n: int) -> str:
        s=""
        if n==0:
            return '0'
        r=1
        while n>0:
            d=n%10
            if r%3==0:
                s='.'+str(d)+s
            else:
                s=str(d)+s
            n=n//10
            r+=1
        if s!='' and s[0]==".":
            s=s[1:]
        return s
