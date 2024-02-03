N = input()
ans = 0

for i in range(len(N) - 1, -1, -1):
    digit = int(N[i])
    div = 2 ** (len(N) - 1 - i)
    ans += digit * div

print(ans)
