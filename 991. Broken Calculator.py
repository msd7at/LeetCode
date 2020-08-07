class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X==Y:
            return 0
        if X>Y:
            return X-Y
        else:
            if Y%2==1:
                return self.brokenCalc(X,Y+1)+1
            else:
                return self.brokenCalc(X,Y//2)+1
