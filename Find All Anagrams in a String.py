class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp=len(p)
        ld=len(s)
        c=[]
        if ld<lp:
            return c
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
            c.append(0)
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
                c.append(i-lp+1)
        return c
 """
 Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
