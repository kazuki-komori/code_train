N = int(input())

#  max 乗を算出する
n = 0

while(True):
    if 2 ** n > N:
        n -= 1
        break
    n += 1

# 答えの配列
ans = []

for i in range(n, -1, -1):
    # 何個入るか
    prime = N // 2 ** i
    if prime > 0:
        ans.append(2 ** i)
        N -= (2**i) * prime


# 答えの出力
print(len(ans))
for a in ans:
    print(a)
