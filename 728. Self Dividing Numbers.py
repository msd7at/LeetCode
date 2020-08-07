class Solution:
    def selfDividingNumbers(self, left, right):
        res = []
        for i in range(left, right+1):
            for char in str(i):
                if int(char)==0 or i % int(char)!=0:
                    break
            else:
                res.append(i)
        return res
