N = int(input())

# 答え
ans = 0
# ダミー変数
n = 0

while True:
    n += 1
    s = str(n)
    if int(s+s) <= N:
        ans += 1
        continue
    break

print(ans)
