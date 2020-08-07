class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        while n>0:
            t=n%10
            s=s+t
            p=p*t
            n=n//10
        return p-s
