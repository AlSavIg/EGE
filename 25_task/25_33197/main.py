from math import sqrt


start = 1000000
stop = 2000000

for i in range(start, stop + 1):
    k = round(sqrt(i))
    count_diff = 0
    for j in range(1, k + 1):
        if i % j == 0:
            if i // j - j <= 100:
                count_diff += 1
    if count_diff >= 3:
        print(i)
