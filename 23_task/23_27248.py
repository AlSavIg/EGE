alf = ("0", "1")

"""
0 -> n + 1
1 -> n * 2
"""

lit_list = []

for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    word = x1 + x2 + x3 + x4 + x5
                    start = 1
                    for lit in word:
                        if lit == "0":
                            start += 1
                        elif lit == "1":
                            start *= 2
                    lit_list.append(start)

min_possible = min(lit_list)

for i in range(min_possible, 100):
    if i not in lit_list:
        print(i)
        break
