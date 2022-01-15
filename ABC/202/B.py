S = input()

ans = ""
for s in S:
    if s == "6":
        ans += "9"
        continue
    if s == "9":
        ans += "6"
        continue
    else:
        ans += s

print(ans[::-1])
