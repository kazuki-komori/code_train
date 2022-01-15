N, Q = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_xk = list(tuple(map(int, input().split())) for _ in range(Q))

def index_multi(l, x):
  return [i for i, _x in enumerate(l) if _x == x]


for xk in arr_xk:
  x = xk[0] # 値
  k = xk[1] # 回数
  
  nx = arr_A.count(x)
  if nx < k:
    print(-1)
    continue
  idx = index_multi(arr_A, x)
  print(idx[k-1]+1)

