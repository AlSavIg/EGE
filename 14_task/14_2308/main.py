def fif(x):
    result = ""
    while x > 0:
        result += str(x % 5)
        x //= 5
    result = result[::-1]
    return result


for i in range(1, 100):
    if fif(i)[len(fif(i)) - 1] == "3" and hex(i)[len(hex(i)) - 1] == "b":
        print(i)
