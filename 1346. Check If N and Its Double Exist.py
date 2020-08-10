class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ar=set(arr)
        for i in ar:
            if i ==0 and arr.count(i)>1:
                return True
            
                
            if i!=0 and i in ar and i*2 in ar:
                return True
        return False
