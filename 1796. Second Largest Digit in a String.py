class Solution:
    def secondHighest(self, s: str) -> int:
        st='1234567890'
        seet=set()
        for i in s:
            if i in st:
                seet.add(int(i))
        if len(seet)<2:
            return -1
        m=max(seet)
        seet.remove(m)
        return max(seet)
        
