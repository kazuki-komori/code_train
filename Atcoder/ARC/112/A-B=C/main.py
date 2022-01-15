from itertools import takewhile
import math
def get_data():
    T = int(input())
    data = [list(map(int, input().split(' '))) for _ in range(T)]
    return T, data

def solve():
    T, data = get_data()
    for d in data:
        L, R = d[0], d[1]
        counter = 0
        for i in range(L, int(math.sqrt(R) + 1)+1):
            x = R - i
            if L <= x <= R - L + 1:
                counter += x - L + 1
        print(counter*2-((L + R)/2 -L))

solve()