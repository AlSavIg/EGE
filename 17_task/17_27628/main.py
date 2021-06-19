start = 3361
stop = 9205
positive = (4, 5)
negative = (9, 11, 17, 23)
count = 0
max_val = -1

for i in range(start, stop + 1):
    result = False
    for j in positive:
        result = result or i % j == 0
    for j in negative:
        result = result and i % j > 0
    if result:
        count += 1
        max_val = max(i, max_val)

print(count, max_val)