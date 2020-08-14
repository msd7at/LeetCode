class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ho=False
        lo=0
        for i in d:
            if d[i]%2==1:
                ho=True
            lo+=(d[i]//2)*2
        if ho:
            lo+=1
        return lo
