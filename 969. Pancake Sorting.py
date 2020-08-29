class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans=[]
        end=len(A)
        def finid(A,end):
            for i in range(len(A)):
                if A[i]==end:
                    return i
        def swap(A,e):
            s=0
            while s<e:
                A[s],A[e]=A[e],A[s]
                s+=1
                e-=1
                
        while end!=1:
            idx=finid(A,end)
            swap(A,idx)
            swap(A,end-1)
            ans.append(idx+1)
            ans.append(end)
            end-=1
        return ans
            
                
