with open("inf_22_10_20_26.txt", "r") as f:
    flag = False
    main_list = []
    border = 50
    for line in f:
        if not flag:
            num = int(line)
            flag = True
        else:
            main_list.append(int(line))
    f.close()
    main_list.sort()
    print(max(main_list))
    for i in range(num):
        if main_list[i] > border:
            bord_index = i
    summary = 0
    for i in range(bord_index, (num - 1 - bord_index) // 2 + 1):
        summary += main_list[i]
    else:
        max_val = main_list[i - 1]
    discount = round(summary * 0.75)
    summary = 0
    for i in range(bord_index + 1):
        summary += main_list[i]
    else:
        summary += discount
print(summary, max_val)

