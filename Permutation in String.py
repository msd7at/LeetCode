class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        lp=len(p)
        ld=len(s)
        if ld<lp:
            return False
        d={}
        for i in p:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        pd={}
        for i in range(lp):
            if s[i] in d:
                if s[i] not in pd:
                    pd[s[i]]=1
                else:
                    pd[s[i]]+=1
        if d==pd:
            return True
        for i in range(lp,ld):
            if s[i-lp] in d:
                if pd[s[i-lp]]>0:
                    pd[s[i-lp]]-=1
                    if pd[s[i-lp]]==0:
                        pd.pop(s[i-lp])
            if s[i] in d:
                if s[i] in pd:
                    pd[s[i]]+=1
                else:
                    pd[s[i]]=1
            if pd==d:
                return True
        return False
  """
  Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
