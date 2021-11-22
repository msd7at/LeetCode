class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i <j:
            a=numbers[i]
            b=numbers[j]
            if a+b == target:
                return [i+1,j+1]
            elif a+b<target:
                i+=1
            else:
                j-=1
