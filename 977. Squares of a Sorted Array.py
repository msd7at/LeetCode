class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i=0
        while i < len(A) and A[i]<0:
            A[i]=-A[i]
            i+=1
        A.sort()
        for i in range(len(A)):
            A[i]=A[i]**2
        return A
        
