class Solution:
    def replaceDigits(self, s: str) -> str:
        ans=s[0]
        ss="1234567890"
        for i in range(1,len(s)):
            if s[i] in ss:
                # print(ord(s[i-1])+int(s[i]))
                # print(chr(ord(s[i-1])+int(s[i])))
                ans=ans+chr(ord(s[i-1])+int(s[i]))
            else:
                ans=ans+s[i]
        return ans
