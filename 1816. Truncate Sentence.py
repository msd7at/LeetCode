class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        c=0
        for i in range(len(s)):
            if s[i]==" ":
                c=c+1
                if c==k:
                    return s[:i]
        return s
        
