with open("27-B_2.txt", "r") as f:
    n = int(f.readline())
    main_list = []
    for line in f:
        x = int(line)
        main_list.append(x)
    f.close()

max_7 = max_2 = max_14 = max_not_14 = 0
main_list.sort(reverse=True)

for i in range(n):
    x = main_list[i]
    if x % 14 == 0:
        max_14 = max(max_14, x)
    elif x % 7 == 0:
        max_7 = max(max_7, x)
    elif x % 2 == 0:
        max_2 = max(max_2, x)
    if x % 14 > 0:
        max_not_14 = max(max_not_14, x)

ans_14 = max_not_14 * max_14
ans_2_7 = max_2 * max_7
answer = max(ans_14, ans_2_7)

print(answer)
