class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=set()
        for i in allowed:
            s.add(i)
        c=1
        for i in words:
            kk=0
            for j in i:
                if j not in s:
                    kk=12
                    break
            if kk==0:
                c+=1
        return c-1
