class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        se=set()
        ans=set()
        for i in range(len(s)-9): 
            if s[i:i+10] not in se:
                se.add(s[i:i+10])
            else:
                ans.add(s[i:i+10])
        return list(ans)
                
                
