class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        c=0
        l1=len(word1)
        l2=len(word2)
        ans=""
        while i<l1 or j<l2:
            if c%2==0:
                if i<l1:
                    ans=ans+word1[i]
                    i+=1
                else:
                    
                    ans=ans+word2[j]
                    j+=1
            else:
                if j<l2:
                    ans+=word2[j]
                    j+=1
                else:
                    ans+=word1[i]
                    i+=1
            c+=1
        return ans
