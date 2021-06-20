with open("27986_B.txt", "r") as f:
    line = int(f.readline())
    main_list = []
    while line != 0:
        main_list.append(line)
        line = int(f.readline())
    f.close()

main_list.sort()
max_7 = 0
max_not_7 = 0
for i in range(len(main_list)):
    if main_list[i] % 7 == 0:
        max_7 = max(max_7, main_list[i])
    else:
        max_not_7 = max(max_not_7, main_list[i])

print(max_not_7 * max_7)

