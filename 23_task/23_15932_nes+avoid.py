def check(a, i):
    global start, stop, condition, avoiding
    if a == avoiding:
        a = 0
        return a
    else:
        belong_segment = a in range(start, stop)
        required = belong_segment if i <= condition else (belong_segment
                                                          and a >= condition)
        a = int(a) if required else 0
        return a


start = 2
stop = 44 + 1
condition = 13
avoiding = 29

path_list = [0] * stop
path_list[start] = 1

for i in range(start + 1, stop):
    path_list[i] = path_list[check(i - 1, i)]\
                   + path_list[check(i / 2, i)]\
                   + path_list[check(i / 3, i)]

print(path_list[stop - 1])
