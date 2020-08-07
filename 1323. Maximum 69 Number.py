class Solution:
    def maximum69Number (self, num: int) -> int:
        """    
        s=str(num)
        a=s.replace("6","9",1)
        return int(a)
                        """
        org=num
        i=0
        j=-1
        while num>0:
            i+=1
            t=num%10
            if t==6:
                j=i
            num=num//10
        if j==-1:
            return org
        return org+ 3*(10**(j-1)) 
                
                
            
                
