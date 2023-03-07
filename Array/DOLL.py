T = int(input())
for i in range(T):
    c = 0
    N, K = list(map(int,input().split()))
    X = list(map(int,input().split()))
    for i in X:
        if i > K:
            c += 1 
    print(c)
