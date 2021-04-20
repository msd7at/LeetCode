class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ar=list(range(1,n+1))
        while len(ar)>1:
            i=(k-1)%len(ar)
            ar.pop(i)
            ar=ar[i:]+ar[:i]
        return ar[0]
                
