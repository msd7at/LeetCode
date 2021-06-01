class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=0
        def abc(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or 0 == grid[i][j] or grid[i][j]=="X":
                return 0
            else:
                grid[i][j]="X"
                return 1+abc(grid,i+1,j)+abc(grid,i,j+1)+abc(grid,i-1,j)+abc(grid,i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                m=max(m,abc(grid,i,j))
        return m
        
