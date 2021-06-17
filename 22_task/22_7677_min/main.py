x_min = 10 ** 10
for x in range(1000, -1, -1):
    a, b = 0, 0
    x_copy = x
    while x > 0:
        a = a + 1
        b = b + x % 100
        x = x // 100
    if a == 2 and b == 13:
        x_min = min(x_copy, x_min)

print(x_min)
