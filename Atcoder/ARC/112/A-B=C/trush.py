def get_data():
    T = int(input())
    data = [list(map(int, input().split(' '))) for _ in range(T)]
    return T, data

def solve():
    T, data = get_data()
    for d in data:
        L, R = d[0], d[1]
        counter = 0
        for i in range(L, R-L+1):
            for j in range(max(i, L), R-L+1):
                sum = i + j
                if sum > R:
                    break
                if i != j:
                    counter += 2
                    continue
                counter += 1
        print(counter)

solve()