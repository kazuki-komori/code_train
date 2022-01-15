s = int(input())
l = list(map(int, input().split()))
l.sort()
d = 0
ans = 0
for i in range(1,len(l)):
    print(l)
    print(d)
    if l[d] != l[i]:
        d = i
    ans += d
    print("///////")
print(ans)