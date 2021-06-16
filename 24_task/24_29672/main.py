with open("inf_22_10_20_24.txt", "r") as f:
    counter = 0
    for line in f:
        if line.count("A") < line.count("E"):
            counter += 1

    print(counter)