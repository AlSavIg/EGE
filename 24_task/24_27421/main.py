with open("24_27421.txt", "r") as f:
    general_str = f.readline()
    f.close()
    counter = 2
    max_len_str = -1
    for i in range(len(general_str) - 2):
        if general_str[i] != general_str[i + 1] != general_str[i + 2]:
            counter += 1
            max_len_str = max(max_len_str, counter)
        else:
            counter = 2

print(max_len_str)