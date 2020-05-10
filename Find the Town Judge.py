class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge=[]
        for i in range(N):
            judge.append([0,0])
        for i in trust:
            o=i[0]
            p=i[1]
            judge[o-1][0]+=1
            judge[p-1][1]+=1
        for i in range(N):
            if judge[i][0]==0 and judge[i][1]==N-1:
                return i+1
        else:
            return -1
        

"""In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1."""
