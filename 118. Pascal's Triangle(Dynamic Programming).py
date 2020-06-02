class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        for i in range(numRows):
            s=[0 for j in range(i+1)]
            s[0],s[-1]=1,1
            for j in range(1,i):
                s[j]=l[i-1][j]+l[i-1][j-1]
            l.append(s)
        return l
                
            
   """
   Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
364,872
Submissions
709,806"""
