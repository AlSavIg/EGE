for num in range(256):
    start_num = num
    num = bin(num).replace("0b", "0" * (10 - len(bin(num))), 1)
    num = num.replace("1", "2")
    num = num.replace("0", "1")
    num = num.replace("2", "0")
    if int(num, 2) - start_num == 133:
        print(start_num)