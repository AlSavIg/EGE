with open("24_demo.txt", "r") as f:
    count = 1
    max_val = -1
    str_file = f.readline()
    for i in range(len(str_file) - 1):
        if str_file[i] == str_file[i + 1] == "Y":
            count += 1
            max_val = max(max_val, count)
        else:
            count = 1

    print(max_val)