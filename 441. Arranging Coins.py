class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1 or n==0:
            return n
        for i in range(1,n+1):
            x=(i*(i+1))//2
            if x>n:
                return i-1
