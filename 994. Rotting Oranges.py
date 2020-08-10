class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r=len(grid)
        if r==0:
            return 0
        c=len(grid[0])
        dis={}
        q=collections.deque()
        lat=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    dis[(i,j)]=0
        while q:
            x,y,d=q.popleft()
            lat=max(lat,d)
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny=dx+x,y+dy
                if 0<= nx < r and 0<=ny<c and grid[nx][ny]==1:
                    grid[nx][ny]=2
                    dis[(nx,ny)]=d+1
                    q.append((nx,ny,d+1))
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    return -1
        return lat
        
        
        
