from collections import Counter
class Solution:

    def numIdenticalPairs(self, num: List[int]) -> int:
        ans=0
        l=Counter(num)
        for i in l:
            if l[i]!=0 or l[i]!=1:
                p=l[i]
                ans+=(p*(p-1))//2
        return ans
