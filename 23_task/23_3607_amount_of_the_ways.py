def check(a):
    belong_segment = a in range(start, stop)
    a = int(a) if belong_segment else 0
    return a


start = 2
n = 50
stop = n + 1

path_list = [0] * stop
path_list[start] = 1

for i in range(start + 1, stop):
    path_list[i] = path_list[check(i - 2)]\
                   + path_list[check(i / 5)]

print(path_list[n])
