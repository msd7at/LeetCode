class Solution:
    def findMaxLength(self, l: List[int]) -> int:
        for i in range(len(l)):
            if l[i]==0:
                l[i]=-1
        s=0
        m=0
        c=0
        d={0:-1}
        for i in l:
            s=s+i
            if s not in d:
                d[s]=c
            else:
                m=max(m,c-d[s])
            c+=1
        return m
        
 """
 Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
