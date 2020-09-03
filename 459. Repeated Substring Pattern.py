#link:https://leetcode.com/problems/repeated-substring-pattern/discuss/826149/Python-3-2-Solutions-(1-less-Runtime-2-Less-Memory)
#Less Runtime (Runtime: 40 ms, faster than 84.41% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14 MB, less than 31.47% of Python3 online submissions for Repeated Substring Pattern.)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l=len(s)
        for i in range(1,(l//2)+1):
            if l%i==0 and s[0:i]*(l//i)==s:
                return True
        return False
#less Memory(Runtime: 272 ms, faster than 16.97% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 13.6 MB, less than 98.29% of Python3 online submissions for Repeated Substring Pattern.)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l=len(s)
        if l%2==1:
            for i in range(1,(l//2)+1,2):
                kp=0
                if l%i==0:
                    to=s[0:i]
                    for j in range(0,l,i):
                        if to!=s[j:j+i]:
                            kp=1
                    if kp==0:
                        return True
            return False
        else:
            for i in range(1,(l//2)+1):
                kp=0
                if l%i==0:
                    to=s[0:i]
                    for j in range(0,l,i):
                        if to!=s[j:j+i]:
                            kp=1        
                    if kp==0:
                        return True
            return False
