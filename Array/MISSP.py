T = int(input())
for i in range(T):
    c = 0
    X = []
    N = int(input())
    for j in range(N):
        X.append(int(input()))
    S = set(X)
    for j in S:
        if X.count(j) % 2 != 0:
            print(j)
    
