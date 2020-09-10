from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
    	s, g, i = list(secret), list(guess), 0
    	while i < len(s):
    		if g[i] == s[i]:
    			del s[i], g[i]
    			i -= 1
    		i += 1
        return str(len(secret)-len(s))+'A'+str(sum((Counter(s)&Counter(g)).values()))+'B'
    
