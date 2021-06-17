x_max = -1
for x in range(1, 10 ** 5):
    a = 0
    b = 1
    x_copy = x
    while x > 0:
        if x % 2 > 0:
            a += x % 12
        else:
            b *= x % 12
        x = x // 12
    if a == 2 and b == 10:
        x_max = max(x_copy, x_max)

print(x_max)
