class Solution:
    def possibleBipartition(self, N: int, dis: List[List[int]]) -> bool:
        d={}
        for i in range(1,N+1):
            d[i]=[]
        for i in dis:
            d[i[0]].append(i[1])
            d[i[1]].append(i[0])
        ar=[0]*(N+1)
        queue=[]
        for i in range(1,N+1):
            if ar[i]==0:
                ar[i]=1
                queue.append(i)
                while len(queue)>0:
                    s=queue.pop(0)
                    for j in d[s]:
                        if ar[j]==ar[s]:
                            return False
                        if ar[j] ==0:
                            ar[j]= -ar[s]
                            queue.append(j)
        return True
"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
