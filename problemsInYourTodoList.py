T = int(input())
for i in range(T):
    c = 0
    N = int(input())
    D = list(map(int,input().split()))
    for i in D:
        if i >= 1000:
            c += 1
    print(c)
