start = 174457
n = 174505
stop = n + 1
dividers_dict = {}
for i in range(start, stop):
    divider = 2
    start_item = i
    dividers_dict[start_item] = []
    while divider ** 2 <= i:
        if i % divider == 0:
            i //= divider
            dividers_dict[start_item].append(divider)
            if len(dividers_dict[start_item]) > 1:
                break
        else:
            divider += 1
    if len(dividers_dict[start_item]) == 1:
        dividers_dict[start_item].append(i)
        key, value = start_item, dividers_dict[start_item]
        # print("Number: {0}\nDividers: {1}    {2}".format(key, *value))
        print(*value)
