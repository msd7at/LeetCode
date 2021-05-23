class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        mlz=0
        mlo=0
        su=0
        cz=0
        co=0
        for i in s:
            i=int(i)
            if su+i==su:
                cz=cz+1
                co=0
            else:
                co=co+1
                cz=0
            su+=i
            mlz=max(mlz,cz)
            mlo=max(mlo,co)
        if mlz>=mlo:
            return False
        return True
            
        
