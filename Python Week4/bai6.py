i_list = list(map(int, input().split(',')))
i_list.sort()
tmp_list = []
o_list = []

for i in range(len(i_list)):
    if i == 0:
        tmp_list.append(i_list[i])
    elif i_list[i] == i_list[i - 1]:
        tmp_list.append(i_list[i])
    else:
        o_list.append(list(tmp_list))
        tmp_list.clear()
        tmp_list.append(i_list[i])

if tmp_list:
    o_list.append(list(tmp_list))

print(o_list)
