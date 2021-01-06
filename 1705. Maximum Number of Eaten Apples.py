class Solution:
    def eatenApples(self, apples: List[int], expire: List[int]) -> int:
        q=[]
        idx=ans=0
        while q or idx<len(apples):
            if idx<len(apples):
                heapq.heappush(q,[expire[idx]+idx,apples[idx]])
            while q and (q[0][0]<=idx or q[0][1]==0):
                heappop(q)
            if q:
                ans+=1
                q[0][1]-=1
            idx+=1
        return ans
