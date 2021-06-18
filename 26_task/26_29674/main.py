with open("inf_22_10_20_26.txt") as f:
    main_list = []
    summary = 0
    flag = False
    for line in f:
        value = int(line)
        if not flag:
            num = value
            flag = True
        else:
            if value > 50:
                main_list.append(value)
            else:
                summary += value

main_list.sort()
num = len(main_list)
for i in range(num):
    if i < num // 2:
        summary += main_list[i] * 0.75
        max_val = main_list[i]
    else:
        summary += main_list[i]

print(round(summary), max_val)