class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        al=len(A)
        bl=len(B)
        a=0
        b=0
        s=[]
        while a<al and b<bl:
            if B[b][0]<=A[a][1] and A[a][0]<=B[b][1]:
                v=[]
                v.append(max(A[a][0],B[b][0]))
                v.append(min(A[a][1],B[b][1]))
                s.append(v)
                if A[a][1]<B[b][1]:
                    a+=1
                elif A[a][1]>B[b][1]:
                    b+=1
                else:
                    a+=1
                    b+=1
            else:
                if A[a][1]<B[b][1]:
                    a+=1
                elif A[a][1]>B[b][1]:
                    b+=1
                else:
                    a+=1
                    b+=1
        return s
    """
    Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
