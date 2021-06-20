start = 120115
stop = 120200
max_length = 0

for i in range(start, stop + 1):
    divider_list = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            divider_list.append(j)
    if len(divider_list) >= max_length:
        max_length = len(divider_list)
        max_item = i

print(max_length + 2, max_item, sep="\n")
