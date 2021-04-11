N = input()
N = N.rstrip("0")

if N == N[::-1]:
    print("Yes")
else:
    print("No")
