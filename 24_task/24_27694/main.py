with open("zadanie24_1 (1).txt", "r") as f:
    main_str = f.readline()
    f.close()
    find_str = ""
    pattern = "AB"
    while main_str.find(find_str) != -1:
        find_str += pattern
    for i in range(len(pattern)):
        if main_str.find(find_str[:-(i + 1)]) == -1:
            continue
        else:
            find_str = find_str[:-(i + 1)]
            break
    print(len(find_str))