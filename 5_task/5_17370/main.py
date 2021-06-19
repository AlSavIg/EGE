num_dict = {}
for i in range(100, 3001):
    start_item = i
    i = list(bin(i).replace("0b", ""))
    for j in range(len(i) - 1):
        if i[j] == "1":
            i[j] = "0"
            break
    i = "".join(i)
    diff = start_item - int(i, 2)
    if not num_dict.get(diff):
        num_dict[diff] = True

print(len(num_dict))
