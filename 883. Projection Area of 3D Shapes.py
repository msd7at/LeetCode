class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        N=len(grid)
        ans=0
        for i in range(N):
            br=0
            bc=0
            for j in range(N):
                if grid[i][j]:
                    ans+=1
                br=max(br,grid[i][j])
                bc=max(bc,grid[j][i])
            ans+=br+bc
        return ans
