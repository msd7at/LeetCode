class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            j= ''.join(sorted(i)) 
            if j in d:
                d[j].append(i)
            else:
                d[j]=[i]
        ar=[]
        for i in d:
            ar.append(d[i])
        return ar
""" Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.""""                
                
         
