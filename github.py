import random

N = 5
loft = [(random.randint(0, 10), random.randint(0, 10)) for x in range(N)]
for item in loft:
    print(item)


def dist(t):
    return t[0] ** 2 + t[1] ** 2


w = list(map(dist, loft))

print(w)
