m = [6,2,5,5,4,5,6,3,7,6]
T = int(input())
for i in range(T):
    x = 0
    a, b = list(map(int,input().split()))
    c = a+b
    while (c != 0):
        t = c % 10
        x += m[t]
        c = c // 10
    print(x)
