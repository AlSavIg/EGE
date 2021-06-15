from random import randint as RI


start = 0
stop = 10 ** 10
for i in range(10 ** 8):
    num = 245245244352
    # result = num in range(10 ** 10)
    result = start <= num <= stop


"""
    result: 13 seconds difference (38 against 25) for range
"""
