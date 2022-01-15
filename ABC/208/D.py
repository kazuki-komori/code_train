import copy
import numpy as np

N, M = map(int, input().split())

path = [list(map(int, input().split())) for _ in range(M)]

path_arr = [[np.inf] * N for _ in range(N)]

for p in path:
    path_arr[p[0]-1][p[1]-1] = p[2]

c_path_arr = copy.deepcopy(path_arr)


def Dycstra(start):
    root = 0
    while True:
        idx = c_path_arr[start].index(min(c_path_arr[start]))
        print(idx)
        break

Dycstra(0)
# print(path_arr[0][2])
print(path_arr)


