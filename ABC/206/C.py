import numpy as np

N = int(input())
A = list(map(int, input().split()))

ans = 0
A_dic = {}

ans_s = []

for a in A:
    if str(a) not in A_dic.keys():
        A_dic[str(a)] = 1
        continue
    A_dic[str(a)] += 1

keys = list(A_dic.keys())
values = list(A_dic.values())
values_arr = []

for (idx, v) in enumerate(values):
    values_arr

for (idx, a_key) in enumerate(A_dic):
    ans_s += (values[idx + 1:] * A_dic[a_key])

print(sum(ans_s))
