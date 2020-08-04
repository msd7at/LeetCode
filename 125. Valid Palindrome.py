class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        se={'1','2','3','4','5','6','7','8','9','0'}
        for i in s:
            if i in se:
                l.append(i)
            elif i.isalpha():
                l.append(i.lower())
        for i in range(len(l)//2):
            if l[i]!=l[-i-1]:
                return False
        return True
        
