N,M = map(int,input().split())
S = [input() for i in range(N)]
T = [input() for i in range(M)]

count = 0
for i in range(N):
    for j in range(M):
        if T[j] == S[i][-3:]:
            count += 1
            break
print(count)