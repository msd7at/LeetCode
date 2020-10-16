class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix==[]:
            return False
        i=0
        j=len(matrix[0])
        if j==0:
            return False
        while i<len(matrix) and matrix[i][0] < target and matrix[i][j-1] <target:
            i+=1
        if i==len(matrix):
            return False
        else:
            if target in matrix[i]:
                return True
        return False
