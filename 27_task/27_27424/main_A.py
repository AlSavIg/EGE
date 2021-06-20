with open("27-A_demo.txt", "r") as f:
    n = int(f.readline())
    value_matrix = []
    max_list = []
    diff_list = []
    for line in f:
        x = list(map(int, line.split()))
        value_matrix.append(x)
        max_list.append(max(x))
        diff_list.append(abs(max(x) - min(x)))
    max_sum = sum(max_list)
    f.close()

result_sum = 0
min_diff = 10 ** 10

for i in range(n):
    if diff_list[i] % 3 != 0:
        min_diff = min(diff_list[i], min_diff)

result_sum = max_sum - min_diff
print(result_sum)
