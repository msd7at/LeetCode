class Solution:
    def squareIsWhite(self, co: str) -> bool:
        a=co[0]
        i=int(co[1])
        if ord(a)%2==0:
            if i%2==0:
                return False
            return  True
        else:
            if i%2==1:
                return False
            return True
