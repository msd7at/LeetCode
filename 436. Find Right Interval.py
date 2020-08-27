class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def bs(ar,tar):
            l=0
            h=len(ar)
            while l<h:
                mid=l+((h-l)//2)
                if ar[mid]<tar:
                    l=mid+1
                else:
                    h=mid
            return l
                
        ar=[]
        d={}
        ans=[0]*len(intervals)
        for i in range(len(intervals)):
            ar.append(intervals[i][0])
            d[intervals[i][0]]=i
        ar.sort()
        for i in range(len(intervals)):
            tm=bs(ar,intervals[i][1])
            if tm==len(intervals):
                ans[i]=-1
            elif tm==0:
                if intervals[i][1]<=ar[0]:
                    ans[i]=d[ar[0]]
                else:
                    ans[i]=-1
            else:
                ans[i]=d[ar[tm]]
        return ans
                    
                    
                    
                    
                    
