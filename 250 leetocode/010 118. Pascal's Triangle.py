class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(numRows):
            if i==0:
                ans.append([1])
            elif i==1:
                ans.append([1,1])
            else:
                ky=[0]*(i+1)
                ky[0]=1
                ky[-1]=1
                # print(ans)
                for j in range(1,i):
                    ky[j]=ans[-1][j]+ans[-1][j-1]
                ans.append(ky)
        return ans
