class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans=[]
        for i in intervals:
            if not ans or ans[-1][1] < i[0]: 
                ans.append(i)
            
            else:
                ans[-1][1]= max(i[1],ans[-1][1])
        return ans
