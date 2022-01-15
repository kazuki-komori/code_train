def get_int():
    return input()

def solve():
    s = get_int()
    length = len(s)-1
    for bit in range(2 ** length):
        ans = int(s[0])
        statement = s[0]
        for i in range(length):
            if (bit >> i) & 1:
                statement += "+"
                ans += int(s[i+1])
            else:
                statement += "-"
                ans -= int(s[i+1])

            statement += s[i+1]
        if ans == 7:
            print(statement + "=7")
            break

solve()