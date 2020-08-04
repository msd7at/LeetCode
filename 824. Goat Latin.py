class Solution:
    def toGoatLatin(self, S: str) -> str:
        s=S.split()
        v={'a','e','i','o','u','A','E','I','O','U'}
        end="a"
        ans=""
        for i in range(len(s)):
            if s[i][0] in v:
                s[i]=s[i]+'ma'
            else:
                t=s[i][0]
                s[i]=s[i][1:]
                s[i]=s[i]+t+'ma'
            s[i]=s[i]+end
            end+='a'
            if i==len(s)-1:
                ans=ans+s[i]
            else:
                ans=ans+s[i]+" "
        return ans
