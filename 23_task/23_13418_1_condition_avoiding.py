def check(a):
    global start, stop, avoiding
    belong_segment = a in range(start, stop)
    requirement = belong_segment and a not in avoiding
    a = int(a) if requirement else 0
    return a


start = 1
stop = 27 + 1
avoiding = (26, -1)

path_list = [0] * stop
path_list[start] = 1

for i in range(start + 1, stop):
    path_list[i] = path_list[check(i - 1)]\
                   + path_list[check((i - 1) / 2)]

print(path_list[stop - 1])
