N = int(input())
a_list = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
x_list = list(map(int, input().split()))

def f1(a, x):
    return a + x

def f2(a, x):
    return max(x, a)

def f3(a, x):
    return min(x, a)

statements = []

for a in a_list:
    if a[1] == 1:
        statements.append(f1)
    if a[1] == 2:
        statements.append(f2)
    if a[1] == 3:
        statements.append(f3)

for x in x_list:
    ans = 0
    for idx, statement in enumerate(statements):
        if idx == 0:
            ans = statement(a_list[idx][0], x)
        ans = statement(a_list[idx][0], ans)
    print(ans)
