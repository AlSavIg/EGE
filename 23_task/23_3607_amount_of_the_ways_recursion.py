def f(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    elif x % 5 == 0:
        return f(x - 2) + f(x // 5)
    else:
        return f(x - 2)


print(f(50))
