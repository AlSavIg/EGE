def check_range(a, i):
    global start, stop, conditions
    belong_gap = a in range(start, stop)
    if i <= conditions[0]:
        requir = belong_gap
    elif conditions[0] < i <= conditions[1]:
        requir = belong_gap and a >= conditions[0]
    elif i > conditions[1]:
        requir = belong_gap and a >= conditions[1]
    a = int(a) if requir else 0
    return a


start = 2
stop = 12 + 1
conditions = (8, 10)

path_amount = [0] * stop
path_amount[start] = 1

for i in range(start + 1, stop):
    path_amount[i] = path_amount[check_range(i - 1, i)]\
                     + path_amount[check_range(i - 2, i)]\
                     + path_amount[check_range(i / 3, i)]

print(path_amount[stop - 1])
