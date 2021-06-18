for x in range(1, 10 ** 4):
    x_start = x
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if L == 4 and M == 5:
        print(x_start)
