class Solution:
    def minOperations(self, n: int) -> int:
        def sums(m):
            return (m*(m+1))//2
        if n==1:
            return 0
        m=n//2
        if n %2 ==0:
            a1=sums(m)
            a2=sums(m-1)
            return a1+a2
        else:
            return 2*sums(m)
