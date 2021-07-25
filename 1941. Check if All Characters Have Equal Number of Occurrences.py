class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        a=[0]*26
        for i in s:
            a[(ord(i)-97)]+=1
        fl=True
        x=0
        for i in a:
            if fl is True and i!=0:
                x=i
                fl=False
            if i!=0 and fl is False and x!=i:
                return False
        return True
