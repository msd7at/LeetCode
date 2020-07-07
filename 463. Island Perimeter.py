# link :   https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        pm=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    if i==0 or grid[i-1][j]!=1:
                        pm+=1
                    if j==0 or grid[i][j-1]!=1:
                        pm+=1
                    if j==c-1 or grid[i][j+1]!=1:
                        pm+=1
                    if i==r-1 or grid[i+1][j]!=1:
                        pm+=1
        return pm
        
