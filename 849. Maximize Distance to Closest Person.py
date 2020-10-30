class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i=0
        j=len(seats)-1
        m=0
        c=0
        if i==0:
            while i<j and seats[i]==0:
                i+=1
                c+=1
            m=max(m,c)
        c=0
        if j==len(seats)-1:
            while i<j and seats[j]==0:
                j-=1
                c+=1
            m=max(m,c)
        li=[]
        for k in range(i,j+1):
            if seats[k]==1:
                li.append(k)
        for i in range(len(li)-1):
            m=max(m,(abs(li[i]-li[i+1])//2))
        return m
                
            
            
                
