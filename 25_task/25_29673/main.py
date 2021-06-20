from math import sqrt


start = 123456789
stop = 223456789

for i in range(start, stop + 1):
    k = round(sqrt(i))
    divider_counter = 0
    max_divider = 1
    if k == sqrt(i):
        for j in range(2, k + 1):
            if i % j == 0:
                divider_counter = divider_counter + 2 if j != k else divider_counter + 1
                max_divider = i // j if max_divider == 1 else max_divider
            if divider_counter > 3:
                break
        if divider_counter == 3:
            print(i, max_divider)
