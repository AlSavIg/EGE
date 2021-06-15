def check_range(a, i):
    global start, stop, conditions
    belong_segment = a in range(start, stop)
    if i <= conditions[0]:
        require = belong_segment
    elif conditions[0] < i <= conditions[1]:
        require = belong_segment and a >= conditions[0]
    elif i > conditions[1]:
        require = belong_segment and a >= conditions[1]
    a = int(a) if require else 0
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
