start = 2422000
stop = 2422080
counter = 1
for i in range(start, stop + 1):
    x = i
    divider = 2
    is_prime = True
    while divider ** 2 <= x:
        if x % divider == 0:
            is_prime = False
            break
        else:
            divider += 1
    if is_prime:
        print(counter, i)
        counter += 1
