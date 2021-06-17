with open("27887.txt", "r") as f:
    max_sum, num = map(int, f.readline().split())
    main_list = []
    for i in range(num):
        main_list.append(int(f.readline()))
    main_list.sort()
    current_sum = 0
    max_index = 0
    while current_sum + main_list[max_index] <= max_sum:
        current_sum += main_list[max_index]
        max_index += 1
    else:
        print(max_index, end=" ")
        max_index -= 1
    memorized = main_list[max_index]
    max_val = -1
    for i in range(max_index, num):
        condition = current_sum - memorized + main_list[i] <= max_sum
        if condition:
            max_val = max(max_val, main_list[i])
    print(max_val)
