N = int(input())
S = input()

ans: str = ""

for s in S:
    c_code = ord(s) + N
    if c_code > 90:
        ans += chr(c_code - 90 + 64)
        continue
    ans += chr(c_code)

print(ans)