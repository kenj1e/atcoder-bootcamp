N = int(input())
S = input()
ans = 0

for i in range(1,N):
    count = 0
    X = S[:i]
    Y = S[i:]
    for c in set(X):
        for d in set(Y):
            if c == d:
                count += 1
                break
        ans = max(ans,count)
print(ans)