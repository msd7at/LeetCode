from collections import Counter 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=collections.Counter(s)
        c=0
        for i in s:
            if d[i]==1:
                return c
            c+=1
        return -1
