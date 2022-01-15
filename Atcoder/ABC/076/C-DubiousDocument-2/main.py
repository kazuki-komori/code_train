sd = input()
t = input()

n = len(sd)
m = len(t)

#sd を後ろから見ていき、tの入りそうな場所を探す
for i in range(n-m,-1,-1):
    tmp = sd[i:i+m]
    print(tmp, i)
    for j in range(m+1):
        if j == m:
            print((sd[:i], t, sd[i+m:]))
            print((sd[:i] + t + sd[i+m:]).replace('?','a'))
            exit()
        if tmp[j] == '?' or tmp[j] == t[j]:
            continue
        else:
            break
    print("//////////")

print('UNRESTORABLE')
