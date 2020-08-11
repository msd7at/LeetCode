class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def back(res,s,open,close,n):
            if len(s)==n*2:
                res.append(s)
                return
            if open < n:
                back(res,s+"(",open+1,close,n)
            if close< open:
                back(res,s+")",open,close+1,n)
        res=[]
        back(res,"",0,0,n)
        return res
        
        
            
