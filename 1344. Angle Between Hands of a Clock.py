class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr=((30*hour)+((1/2)*minutes))
        mi=minutes*6 
        x=abs(hr-mi)
        if x>180:
            return(360-x)
        return(x)
