S1 = input()
S2 = input()
S3 = input()

S = S1 + S2 + S3
S = list(set(S))

D = dict(zip(S, [1] * len(S)))

# for i in range(9)

def parse(S, D):
    res = ""
    for s in S:
        res += str(D[s])
    return res

print(parse(S1, D))