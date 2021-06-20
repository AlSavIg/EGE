from math import sqrt


start = 125256
stop = 125330

for i in range(start, stop + 1):
    k = round(sqrt(i))
    divider_list = []
    if i % 2 == 0:
        divider_list.append(i)
        for j in range(2, k + 1):
            if i % j == 0:
                if j % 2 == 0:
                    divider_list.append(j)
                if (i // j) % 2 == 0 and (i // j) != k:
                    divider_list.append(i // j)
            if len(divider_list) > 6:
                break
    if len(divider_list) == 6:
        divider_list.sort()
        print("{:2d} {:2d} {:2d} {:2d} {:2d} {:2d}".format(*divider_list))
