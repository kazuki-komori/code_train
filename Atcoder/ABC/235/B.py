N = int(input())
Hs = list(map(int, input().split()))


for now, h in enumerate(Hs):
  if now == len(Hs)-1:
    print(h)
    exit()
  if h >= Hs[now + 1]:
    print(h)
    exit()