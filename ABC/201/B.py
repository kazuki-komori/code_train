N = int(input())
inputs = [input().split() for _ in range(N)]

mountains = []

for i in inputs:
    mountains.append(dict(name=i[0], height=int(i[1])))

mountains_sorted = sorted(mountains, key=lambda x:x["height"], reverse=True)

print(mountains_sorted[1]["name"])
