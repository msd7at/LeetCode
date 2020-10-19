class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A)<=1:
            return 1
        def help(target,A,B):
            c=0
            for i in range(len(B)):
                a,b=A[i],B[i]
                if target==a:
                    continue
                else:
                    if b is not target:
                        c=float("inf")
                        break
                    else:
                        c+=1
            return c
        ans=min(help(A[0],A,B),help(A[0],B,A),help(B[0],A,B),help(B[0],B,A))
        if ans == float("inf"):
            return -1
        else:
            return ans
