class Solution:
    def maximumUniqueSubarray(self, l: List[int]) -> int:
        s=set()
        st=0
        c=0
        mi=-10000
        for i in range(len(l)):
            if l[i] not in s:
                s.add(l[i])
                c+=l[i]    
            else:
                while l[st]!=l[i]:
                    c-=l[st]
                    s.remove(l[st])
                    st+=1
                c-=l[st]
                s.remove(l[st])
                st+=1
                c+=l[i]
                s.add(l[i])

            mi=max(c,mi)
            
        return mi
                
                
            
