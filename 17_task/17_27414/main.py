start = 1016
stop = 7937
positive = 3
negative = (7, 17, 19, 27)
max_val = -1
count = 0

for i in range(start, stop + 1):
    result = i % positive == 0
    if result:
        for j in negative:
            result = result and i % j > 0
    else:
        continue
    if result:
        count += 1
        max_val = max(max_val, i)

print(count, max_val)