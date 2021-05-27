class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        valc=[]
        for i in range(len(s)):
            if s[i]==c:
                valc.append(i)
        ans=[]
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
            else:
                vtba=abs(i-valc[0])
                for j in valc:
                    if vtba>=abs(i-j):
                        vtba=abs(i-j)
                    else:
                        break
                ans.append(vtba)
        return ans
                
        
