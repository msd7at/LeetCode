class Solution:
    def numberOfMatches(self, n: int) -> int:
        def rec(n):
            if n==1:
                return 0
            if n%2:
                return 1+(n//2)+rec(n//2)
            else:
                return (n//2)+rec(n//2)
        return rec(n)
