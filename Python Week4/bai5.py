lists = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
flattened_list = []
for lst in lists:
    if isinstance(lst, list):
        for i in lst:
            flattened_list.append(i)
    else:
        flattened_list.append(lst)
print(flattened_list)
