class Solution:
    def makeGood(self, s: str) -> str:
        if len(s)==0:
            return s
        for t in range(100):  # for checking again if there is any other merged bad characters
            i=0
            while i + 1 < len(s):
                if abs(ord(s[i])-ord(s[i+1])) == 32 :  #for checking two adjacent characters  i.e ord('a') - ord('A') = 32
                    s = s[:i]+ s[i+2:]    #for removing both bad characters from string 
                else:
                    i+=1
        return s
        
