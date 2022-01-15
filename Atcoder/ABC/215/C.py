import itertools

S, K = input().split()
data = list(S)
per_list = itertools.permutations(data)
dic_arr = []
for case in per_list: 
  dic_arr.append("".join(case))

dic_arr = sorted(list(set(dic_arr)))


print(dic_arr[int(K)-1])
