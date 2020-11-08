class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        l=[0]*(n+1)
        if n==0:
            return 0
        l[1]=1
        for i in range(1,(n+1)//2):
            l[2*i]=l[i]
            l[2*i + 1]= l[i]+l[i+1]
        print(l)
        return max(l)
