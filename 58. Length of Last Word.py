class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ss=0
        c=0
        idd=len(s)-1
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                idd=idd-1
            else:
                break
        for i in range(idd,-1,-1):
            if s[i]==" ":
                ss=max(ss,c)
                c=0
                break
            else:
                c+=1
        return(max(ss,c))
