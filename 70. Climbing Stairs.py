# link:70. Climbing Stairs  https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n<=1:
                return 1 
            if self.ar[n]>0:
                return self.ar[n]
            op1=fib(n-1)
            op2=fib(n-2)
            self.ar[n]=op1+op2
            return op1+op2
        self.ar=[0]*(n+1)
        return fib(n)
