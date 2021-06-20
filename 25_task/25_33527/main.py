from math import sqrt


start = 101000000
stop = 102000000

for i in range(start, stop + 1):
    if i % 2 == 0:
        count = 1
        k = round(sqrt(i))
        for j in range(2, k + 1):
            if i % j == 0:
                if j % 2 == 0:
                    count += 1
                if (i // j) % 2 == 0 and (i // j) != k:
                    count += 1
                if count > 3:
                    break
    else:
        count = 0

    if count == 3:
        print(i)
