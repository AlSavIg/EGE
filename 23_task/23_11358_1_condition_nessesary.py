def check_range(a, i):
    global start, stop, condition
    belong_segment = a in range(start, stop)
    requir = belong_segment if i <= condition else (belong_segment and a >= condition)
    a = int(a) if requir else 0
    return a


start = 3
stop = 12 + 1
condition = 10

amount_path = [0] * stop
amount_path[3] = 1

for i in range(start + 1, stop):
    amount_path[i] = amount_path[check_range(i - 1, i)]\
                     + amount_path[check_range(i - 2, i)]\
                     + amount_path[check_range(i / 2, i)]

print(amount_path[stop - 1])
