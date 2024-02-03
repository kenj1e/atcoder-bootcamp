N,K = map(int, input().split())

ans = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if K - i - j <= N  and K - i - j >= 1:
            ans += 1
print(ans)

# C++であれば終値を<=Nで指定できるが、pythonではN+1まで指定する必要がある。