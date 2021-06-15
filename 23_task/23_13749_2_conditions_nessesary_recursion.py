def f(x):
    global conditions
    if x < 2:
        return 0
    elif x == 2:
        return 1
    elif i % 3 == 0:
        return f(x - 1) + f(x - 2) + f(x // 3)


def g(x):
    global conditions
    if x <= conditions[0]:
        return f(x)
    elif conditions[0] < x <= conditions[1]:
        pass


start = 2
stop = 12 + 1
conditions = (8, 10)

