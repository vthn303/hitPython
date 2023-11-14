n = int(input('nhap n = '))
i_list = list(map(str,input().split()))
o_list = []
if len(i_list) % n != 0:
    print(f'khong the tach list thanh {n} list-child')
else:
    for i in range(n):
        o_list.append(i_list[i::n])
print(o_list)


