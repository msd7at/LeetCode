class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[]
        for i in range(m):
            s=[]
            for j in range(n):
                s.append(0)
            l.append(s)
        for i in range(m):
            l[i][0]=1
        for j in range(n):
            l[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                l[i][j]=l[i-1][j]+l[i][j-1]
        return l[m-1][n-1]
       
  """
  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?"""
