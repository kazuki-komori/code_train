import sys
sys.setrecursionlimit(10**7)
h,w = map(int, input().split())
c = [list(input()) for i in range(h)]

def search(x, y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#" or c[x][y] == "$":
        return
    if c[x][y] == "g":
        print("Yes")
        sys.exit()
    c[x][y] = "$"
    search(x + 1, y)
    search(x - 1, y)
    search(x, y + 1)
    search(x, y - 1)

sx = 0
sy = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx = i
            sy = j
            break

search(sx, sy)
print("No")