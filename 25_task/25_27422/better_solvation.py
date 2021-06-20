from math import sqrt


start = 174457
stop = 174505
# Two dividers ONLY (not include 1 and number itself)
for i in range(start, stop + 1):
    divider_list = []
    k = round(sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            divider_list.append(j)
            if (i // j) != k:
                divider_list.append(i // j)
        if len(divider_list) > 2:
            break
    if len(divider_list) == 2:
        print(*divider_list)
