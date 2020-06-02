class Solution:
    def balancedStringSplit(self, s: str) -> int:
        co=0
        c=0
        for i in s:
            if i=="L":
                c+=1
            else:
                c=c -1
            if c==0:
                co+=1
        return co
    
 """
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

"""
