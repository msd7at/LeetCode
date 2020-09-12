class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def back(rem,com,ns):
            if rem==0 and len(com)==k:
                result.append(list(com))
                return
            elif rem<0 or len(com)==k:
                return 
            for i in range(ns,9):
                com.append(i+1)
                back(rem-i-1,com,i+1)
                com.pop()
        back(n,[],0)
        return result
