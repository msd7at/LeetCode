class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        R=[]
        C=[]
        r=len(grid)
        c=len(grid[0])
        rm=0
        cm=0
        for i in range(r):
            cm=0
            rm=0
            for j in range(c):
                cm=max(cm,grid[j][i])
                rm=max(rm,grid[i][j])
            C.append(cm)
            R.append(rm)
        ans=0
        for i in range(r):
            for j in range(c):
                ans=ans + (min(R[i],C[j]))- grid[i][j]
        return ans
