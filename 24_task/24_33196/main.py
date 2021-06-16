with open("24.txt", "r") as f:
    main_str = f.readline()
    f.close()
    after_A = {}
    for i in range(len(main_str) - 1):
        if main_str[i] == "A":
            if after_A.get(main_str[i + 1]):
                after_A[main_str[i + 1]] += 1
            else:
                after_A[main_str[i + 1]] = 1

    print(list(after_A.items())[list(after_A.values()).index(max(after_A.values()))])