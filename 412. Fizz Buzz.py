class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a="Fizz"
        b="Buzz"
        aa=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                aa.append(a+b)
            elif i%3==0:
                aa.append(a)
            elif i%5==0:
                aa.append(b)
            else:
                aa.append(str(i))
        return aa
