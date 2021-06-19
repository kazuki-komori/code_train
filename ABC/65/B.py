N = int(input())
buttons = list(int(input()) for _ in range(N))

arr_idx = 100000
idx = 1
n = 0

for _ in range(arr_idx):
    idx = buttons[idx-1]
    n += 1
    if idx == 2:
        print(n)
        exit()

print(-1)
