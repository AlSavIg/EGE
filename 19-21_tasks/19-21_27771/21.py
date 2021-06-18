def f(s1, s2, turn):
    global min_sum
    if turn == 4:
        if s1 + s2 <= min_sum:
            return True
        else:
            return False
    if turn == 3:
        return f(max(s1, s2) // 2, min(s1, s2), turn + 1)
    if turn == 2:
        if s1 + s2 - 1 <= min_sum or s1 // 2 + s2 <= min_sum or s2 // 2 + s1 <= min_sum:
            return False
        else:
            return f(s1 - 1, s2, turn + 1) \
                   and f(s1, s2 - 1, turn + 1) \
                   and f(s1 // 2, s2, turn + 1) \
                   and f(s1, s2 // 2, turn + 1)
    if turn == 1:
        if s1 + s2 - 1 <= min_sum or s1 // 2 + s2 <= min_sum or s2 // 2 + s1 <= min_sum:
            return True
        else:
            return f(s1 - 1, s2, turn + 1) \
                   or f(s1, s2 - 1, turn + 1) \
                   or f(s1 // 2, s2, turn + 1) \
                   or f(s1, s2 // 2, turn + 1)
    if turn == 0:
        if s1 + s2 - 1 <= min_sum or s1 // 2 + s2 <= min_sum or s2 // 2 + s1 <= min_sum:
            return False
        else:
            return f(s1 - 1, s2, turn + 1) \
                   and f(s1, s2 - 1, turn + 1) \
                   and f(s1 // 2, s2, turn + 1) \
                   and f(s1, s2 // 2, turn + 1)


min_sum = 20
s1 = 10
turn = 0

for s2 in range(100, 9, -1):
    if f(s1, s2, turn):
        print(s2, end=" ")
