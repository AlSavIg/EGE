def f(S1, S2, turn):
    global max_sum
    # + 1 // * 2 // >= 77 // S1 = 7 // Petya first (% 2 == 0): 0, 2 // Vanya second (% 2 == 1): 1, 3
    # P V P V
    # 0 1 2 3
    if turn == 2:
        if S1 + S2 >= max_sum:
            return True
        else:
            return False
    elif turn < 2 and S1 + S2 >= max_sum:
        return False
    else:
        return f(S1 + 1, S2, turn + 1) \
               or f(S1, S2 + 1, turn + 1) \
               or f(S1 * 2, S2, turn + 1) \
               or f(S1, S2 * 2, turn + 1)


max_sum = 77
S1 = 7
turn = 0

for S2 in range(69, -1, -1):
    if f(S1, S2, turn):
        print(S2)
