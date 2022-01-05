class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        l= len(s)
        j=0
        for i in range(l):
            if j<len(spaces) and spaces[j]==i:
                ans.append(" "+s[i])
                j+=1
            else:
                ans.append(s[i])
            # print(ans)
        return "".join(ans)
