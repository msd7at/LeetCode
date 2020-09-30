class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans=0
        for i in logs:
            c=i.count(".")
            if c==0:
                ans+=1
            elif c==2:
                if ans!=0:
                    ans-=1
        return ans
                
