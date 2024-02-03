N,X= map(int, input().split())
A = list(map(int, input().split()))
ans = False

for i in range(N):
    if A[i] == X:
        ans = True
        print("Yes")
        exit()
if ans == False:
    print("No")