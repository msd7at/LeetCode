class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            a=0
            b=len((A[0]))-1
            while a<=b:
                if a==b:
                    if A[i][a]:
                        A[i][a]=0
                    else:
                        A[i][a]=1
                else:
                    a1=A[i][a]
                    a2=A[i][b] 
                    if a2:
                        A[i][a]=0
                    else:
                        A[i][a]=1
                    if a1:
                        A[i][b]=0
                    else:
                        A[i][b]=1
                a+=1
                b-=1
        return A
                   
