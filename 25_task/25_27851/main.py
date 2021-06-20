start = 210235
stop = 210300

for i in range(start, stop + 1):
    divider_list = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            divider_list.append(j)
        if len(divider_list) > 4:
            break
    if len(divider_list) == 4:
        print(*divider_list)