class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        x=math.log(num,4)
        return int(x)==x       
