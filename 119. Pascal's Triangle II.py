class Solution:
    def getRow(self, k: int) -> List[int]:
        l=[1]*(k+1)
        for j in range(1,k+1):
            a=l[0]
            b=l[1]
            for i in range(1,j):
                l[i]=a+b
                a=b
                b=l[i+1]
        return l
