N= int(input())

for i in range(9,-1,-1):
    div = (1<<i)
    print((N//div)%2, end="")

