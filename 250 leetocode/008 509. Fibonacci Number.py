class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        a=0
        b=1
        s=0
        for i in range(1,n):
            x=b
            b=a+b
            a=x
        return b
            
