import copy
h, w = 10, 10
shima = [list(input()) for _ in range(h)]


def dfs(x, y, c_shima):
    if not(0 <= x < h) or not(0 <= y < w) or not(c_shima[x][y] == "o"):
        return

    c_shima[x][y] = "$"
    dfs(x+1, y, c_shima)
    dfs(x-1, y, c_shima)
    dfs(x, y+1, c_shima)
    dfs(x, y-1, c_shima)


def judge(c_shima):
    for k in range(h):
        for l in range(w):
            if c_shima[k][l] == "o":
                return
    print("YES")
    exit()


for i in range(h):
    for j in range(w):
        c_shima = copy.deepcopy(shima)
        c_shima[i][j] = "o"
        dfs(i, j, c_shima)
        judge(c_shima)

print("NO")
