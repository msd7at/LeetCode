class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        if len(matrix) == 0:
            return []
        rs=0
        cs=0
        re=len(matrix)-1
        ce=len(matrix[0])-1
        
        while rs <= re and cs <= ce:
            for i in range(cs,ce+1):
                res.append(matrix[rs][i])
            rs+=1
            for i in range(rs,re+1):
                res.append(matrix[i][ce])
            ce-=1
            if rs<= re:
                for i in range(ce,cs-1,-1):
                    res.append(matrix[re][i])
                re-=1
            if cs <= ce:
                for i in range(re,rs-1,-1):
                    res.append(matrix[i][cs])
                cs+=1
        return res
                    
