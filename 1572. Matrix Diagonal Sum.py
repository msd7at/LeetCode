class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l=len(mat)
        s=0
        c=l-1
        for i in range(l):
            s=s+mat[i][i]
            if i<(l//2):
                s=s+mat[i][c]
                s=s+mat[c][i]
            c-=1
        return s
