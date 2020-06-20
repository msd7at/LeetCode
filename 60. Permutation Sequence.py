class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=factorial(n-1)
        k=k-1
        ans=""
        li=list(range(1,n+1))
        for i in range(n-1,0,-1):
            idx=int(k//fact)
            ans=ans+str(li[idx])
            li.pop(idx)
            k=k%fact
            fact=fact/i
        ans=ans+str(li[0])
        return("".join(ans))
            
