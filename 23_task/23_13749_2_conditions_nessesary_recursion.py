def f(x):
    global conditions
    if x < 2:
        return 0
    elif x == 2:
        return 1
    if x <
    elif i % 3 == 0:
        return f(x - 1) + f(x - 2) + f(x // 3)



start = 2
stop = 12 + 1
conditions = (8, 10)

path_amount = [0] * stop
path_amount[start] = 1

for i in range(start + 1, stop):
    path_amount[i] = path_amount[check_range(i - 1, i)]\
                     + path_amount[check_range(i - 2, i)]\
                     + path_amount[check_range(i / 3, i)]
