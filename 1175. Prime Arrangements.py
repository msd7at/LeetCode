class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes=[True for _ in range(n+1)]
        for i in range(2,int(((n+1)//2 )+1)):
            if primes[i]:
                for j in range(i**2,n+1,i):
                    primes[j]=False
        
        s=sum(primes[2:])
        x=factorial(s)
        y=factorial(n-s)
        return (x*y) % (10 ** 9 + 7)
