class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans=""
        for i in s:
            ans+=str(ord(i)-96)
        for i in range(k):
            su=0
            ss=""
            for j in ans:
                
                su=su+int(j)
                
            ans=str(su)
        return su
                
