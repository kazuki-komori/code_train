import itertools

A, B, K = map(int, input().split())

n = "0" * A + "1" * B

# print(bin(K)[2::] + n)
# print(set(list(itertools.permutations(n, A + B))))
# L = set(list(itertools.permutations(n, A + B)))
# ls = []
# for l in L:
#     ls.append(str("".join(l)))
#
# ls.sort()
a = int(n, 2)
counter = 0
while(True):
    if counter == K:
        break
    a += 1
    if bin(a)[2::].count("0") != A:
        continue
    counter += 1
ans = bin(a)[2::]
print(ans)
ans = ans.replace("1", "b")
ans = ans.replace("0", "a")
print(ans)
# print(int(n, 2))
# print(bin(n))
# print(bin(K)[2::])
