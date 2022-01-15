def solve():
    s = set_int()
    ans = 0
    for bit in range(2 ** (len(s)-1)):
        index = s[0]
        for j in range(len(s)-1):
            if (bit >> j) & 1:
                index += "+"
            index += s[j+1]
        ans += sum(map(int, index.split("+")))
    print(ans)


def set_int():
    return input()

solve()
