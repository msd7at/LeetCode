class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l=0
        r=len(A)-1
        while l<r:
            while l<r and A[l]%2==0:
                l+=1
            while l<r and A[r]%2==1:
                r-=1
            A[l],A[r]=A[r],A[l]
        return A
