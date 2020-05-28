
t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=min(l)
    s=-(m*m)
    for i in l:
        s=s+(i*m)
    print(s)
