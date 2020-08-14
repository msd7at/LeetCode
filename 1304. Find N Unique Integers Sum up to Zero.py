class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=[0]*(n)
        k=n
        for i in range(n//2):
            a[i]=k
            a[-i-1]=-k
            k-=1
        return a
