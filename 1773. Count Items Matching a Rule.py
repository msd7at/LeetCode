class Solution:
    def countMatches(self, Lists: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type" :
            idd=0
        elif ruleKey == "color" :
            idd=1
        else:
            idd=2
        c=0
        
        for i in range(len(Lists)):
            if Lists[i][idd]==ruleValue:
                c+=1
        return c
