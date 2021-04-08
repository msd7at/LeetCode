class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        coll={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return ''
        res=[]
        
        def rec(idx,ans):
            if len(ans)==len(digits):
                res.append(ans)
                return
            for q in coll[digits[idx]]:
                ans+=q
                rec(idx+1,ans)
                ans=ans[:-1]
            
        rec(0,"")
        return res
        
