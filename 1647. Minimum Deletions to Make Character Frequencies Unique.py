from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=Counter(s)
        d={}
        cost=0
        for i in c.items():
            if i[1] in d:
                a=i[1]
                while a in d and a>0:
                    a-=1
                    cost+=1
                d[a]=0
            else:
                d[i[1]]=0
        return cost
