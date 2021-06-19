start = 101000000
stop = 102000000

for i in range(start, stop + 1):
    if i % 2 == 0:
        dividers_count = 1
        for j in range(3, i // 2 + 1):
            condition = i % j == 0
            if condition and j % 2 > 0:
                dividers_count = 0
                break
            elif condition:
                dividers_count += 1
            if dividers_count > 3:
                break
    else:
        dividers_count = 0
    if dividers_count == 3:
        print(i)
