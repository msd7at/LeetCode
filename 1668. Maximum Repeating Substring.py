class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        x=len(sequence)
        y=len(word)
        i=0
        while i<(x-y+1):
            if sequence[i:i+y]==word:
                o=0
                while i<(x-y+1) and sequence[i:i+y]==word:
                    o+=1
                    i+=y
                k=max(o,k)
                    
            else:
                i+=1
        return k
