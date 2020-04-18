class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S=[]
        c=0
        for i in s:
            if i!="#":
                S.append(i)
                c+=1
            else:
                if c!=0:
                    S.pop()
                    c=c-1
        T=[]
        c=0
        for i in t:
            if i!="#":
                T.append(i)
                c+=1
            else:
                if c!=0:
                    T.pop()
                    c=c-1
        if T==S:
            return"true"
        else:
            "false"
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

  
        
