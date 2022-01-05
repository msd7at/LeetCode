class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l=len(i)-1
            j=0
            while j<l and i[j] == i[l]:
                j+=1
                l-=1
            if j>=l:
                return i
        return ""
            
