N, Q = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_xk = list(tuple(map(int, input().split())) for _ in range(Q))

def search_half(arr, x, k, counter = 0, idx = 1, next = []):
  half = len(arr)//2
  bef = arr[:half]
  aft = arr[half:]
  if len(next) == 0:
    half = len(arr)//2
    bef = arr[:half]
    aft = arr[half:]
  else:
    half = len(next)//2
    bef = next[:half]
    aft = next[half:]
  # print("{} {} idx = {} count = {}".format(bef, aft, idx, counter))
  if (len(next) == 1):
    counter += 1
    if  k == counter:
      return idx
    idx += 1
    return search_half(arr, x, k, counter, idx, arr[idx-1:])
  if x in bef:
    # print("bef")
    return search_half(arr, x, k, counter, idx, next=bef)
  else:
    idx += len(bef)
    # print("aft")
    return search_half(arr, x, k, counter, idx, next=aft)

for xk in arr_xk:
  x = xk[0] # 値
  k = xk[1] # 回数
  # print("//////////////{} {}".format(x, k))
  
  nx = arr_A.count(x)
  if nx < k:
    print(-1)
    continue
  idx = search_half(arr_A, x, k)
  print(idx)

