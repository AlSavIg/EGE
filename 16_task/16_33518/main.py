def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n // 2)
    elif n % 2 > 0:
        return 1 + f(n - 1)


for i in range(10 ** 5, -1, -1):
    if f(i) == 12:
        min_val = i

print(min_val)
