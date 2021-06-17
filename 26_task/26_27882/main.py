with open("27882.txt", "r") as f:
    max_sum, num = map(int, f.readline().split())
    main_list = []
    for line in f:
        main_list.append(int(line))
    f.close()
    main_list.sort()
    elements = []
    max_val = -1
    len_elem = 0
    while sum(elements) + main_list[len_elem] <= max_sum:
        elements.append(main_list[len_elem])
        len_elem += 1
    for j in range(len_elem, num - 1):
        condition = sum(elements) - max(elements) + main_list[j] <= max_sum
        if condition:
            max_val = max(max_val, main_list[j])
    elements[len(elements) - 1] = max_val

print(len(elements), max(elements))
