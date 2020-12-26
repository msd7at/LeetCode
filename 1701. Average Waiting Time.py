class Solution:
    def averageWaitingTime(self, cs: List[List[int]]) -> float:
        n=len(cs)
        t=0
        s=cs[0][0]+cs[0][1]
        t=s-cs[0][0]
        # print(s,t)
        for i in cs[1:]:
            if s<i[0]:
                s=i[0]
            s=s+i[1]
            if s<i[0]:
                s=i[0]+i[1]
            t=t+s-i[0]
            # print(s,t)
        return t/n
