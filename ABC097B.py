N = int(input())
ans = 0
for i in range(1,50):
    for j in range(2,50):
        if i**j <= N:
            ans = max(ans,i**j)
print(ans)

# どこまで探索すべきかがわからないので、とりあえず50まで探索してみたら通った。