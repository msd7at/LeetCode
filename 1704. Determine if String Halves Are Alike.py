class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)
        d1={'vo':0,"etc":0}
        v="aeiou"
        d2={'vo':0,"etc":0}
        for i in s[0:l//2]:
            i=i.lower()
            if i in v:
                d1["vo"]+=1
            else:
                d1["etc"]+=1
        for i in s[l//2:]:
            i=i.lower()
            if i in v:
                d2["vo"]+=1
            else:
                d2["etc"]+=1
        return True if d1==d2 else False
