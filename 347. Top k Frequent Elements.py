class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        new = [(value, key) for key, value in d.items()]
        new.sort(reverse=True)
        s=0
        a=[]
        for i in range(k):
            a.append(new[i][1])                
        return a
        
