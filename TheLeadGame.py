T = int(input())
sp1 = 0
sp2 = 0
lead = 0
leader = -1
for i in range(T):
    S = list(map(int,input().split()))
    sp1 += S[0]
    sp2 += S[1]
    #print(abs(sp1-sp2))
    if lead < abs(sp1-sp2):
        lead = abs(sp1-sp2)
        if sp1 > sp2:
            leader = 1
        else:
            leader = 2
print(leader,lead)
