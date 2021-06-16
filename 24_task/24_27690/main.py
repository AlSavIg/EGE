with open("zadanie24_1.txt", "r") as f:
    main_str = f.readline()
    f.close()
    max_len = -1
    count = 1
    for i in range(len(main_str) - 1):
        if main_str[i] != main_str[i + 1]:
            count += 1
            max_len = max(max_len, count)
        else:
            count = 1

    print(max_len)