with open("24_demo.txt", "r") as f:
    general_str = f.readline()
    f.close()
    find_str = ""
    while general_str.find(find_str) != -1:
        find_str += "XYZ"
    for i in range(3):
        if general_str.find(find_str[:-(i + 1)]) == -1:
            continue
        else:
            find_str = find_str[:-(i + 1)]
            break

print(len(find_str))
