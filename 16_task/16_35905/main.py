def f(n):
    if n == 0:
        return 0
    elif n % 3 > 0:
        return n % 3 + f(n - n % 3)
    elif n % 3 == 0:
        return f(n // 3)


for i in range(1000, -1, -1):
    if f(i) == 9:
        min_val = i

print(min_val)