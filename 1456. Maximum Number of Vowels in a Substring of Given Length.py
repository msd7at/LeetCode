class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=len(s)
        if l<k:
            return 0
        else:
            c=0
            d={}
            for i in range(k):
                if s[i]== 'a' or s[i] =='e' or s[i]=="i" or s[i]=="o" or s[i]=="u":
                    if s[i] in d:
                        d[s[i]]+=1
                        c+=1
                    else:
                        d[s[i]]=1
                        c+=1
            if l==k:
                return c
            m=0
            m=max(m,c)
            for i in range(k,l):
                if s[i-k]== 'a' or s[i-k] =='e' or s[i-k]=="i" or s[i-k]=="o" or s[i-k]=="u":
                    c=c-1
                    if d[s[i-k]]==1:
                        d.pop(s[i-k])
                    else:
                        d[s[i-k]] -=1
                if s[i]== 'a' or s[i] =='e' or s[i]=="i" or s[i]=="o" or s[i]=="u":
                    if s[i] in d:
                        d[s[i]]+=1
                        c+=1
                    else:
                        d[s[i]]=1
                        c+=1
                m=max(m,c)
        return m
        """
        Given a string s and an integer k.

Return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are (a, e, i, o, u).

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
Example 4:

Input: s = "rhythms", k = 4
Output: 0
Explanation: We can see that s doesn't have any vowel letters.
Example 5:

Input: s = "tryhard", k = 4
Output: 1
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters.
1 <= k <= s.length"""
