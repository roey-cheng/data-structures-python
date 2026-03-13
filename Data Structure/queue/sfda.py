values = [4, 9, 12, 3, 7, 26, 16, 20, 11]
h = [None] * 13
for v in values:
    i = v % 13
    while h[i] is None:
        i = (i + 1) % 13
    h[i] = v
print(h)