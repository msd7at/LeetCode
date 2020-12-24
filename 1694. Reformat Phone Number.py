class Solution:
    def reformatNumber(self, number: str) -> str:
        se={"1","2","3","4","5","6","7","8","9","0"}
        s=""
        for i in number:
            if i in se:
                s+=i
        l=len(s)
        ans=""
        for i in range(l): 
            if i%3==0 and i!=0:
                ans+="-"
            if l-i==4 and i%3==0:
                if ans!="" and ans[-1]!="-":
                    ans+="-"
                for j in range(2):
                    ans+=s[i]
                    i+=1
                ans+="-"
                for j in range(2):
                    ans+=s[i]
                    i+=1
                break
            ans+=s[i]     
        return ans
            
                
            
                
            
            
                
                
        
                
