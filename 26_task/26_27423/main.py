with open("26_demo.txt", "r") as f:
    max_sum, num = map(int, f.readline().split())
    elem_list = []
    main_list = []
    max_elem = -1
    for line in f:
        main_list.append(int(line))
    f.close()
    main_list.sort()
    item = 0
    while sum(elem_list) + main_list[item] <= max_sum:
        elem_list.append(main_list[item])
        item += 1
    for j in range(item, num - 1):
        tested_sum = sum(elem_list) - max(elem_list) + main_list[j]
        if tested_sum <= max_sum:
            max_elem = max(max_elem, main_list[j])
    elem_list[item - 1] = max_elem if max_elem > 0 else elem_list[item - 1]

print(len(elem_list), end=" ")
print(max(elem_list))
