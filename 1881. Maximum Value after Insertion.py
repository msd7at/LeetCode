class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if int(n)>0:
            for i in range(len(n)):
                if int(n[i])<x:
                    return n[0:i]+str(x)+n[i:] 
            return n+str(x)
        elif int(n)==0:
            return str(x)+n
        else:
            for i in range(1,len(n)):
                if int(n[i])>x:
                    return n[0:i]+str(x)+n[i:]
            return n+str(x)
                
            
                
        
