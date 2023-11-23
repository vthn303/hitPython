def display():
    for key, value in setup_dict.items():
        print(f'{key}:{value}')

setup_dict = {'SV01': 2.0,
            'SV02':3.5,
            'SV03':4.5,
            'SV04':1.5,
            'SV05':2.5
            }
display()
sum = 0
for point in setup_dict.values():
    if 2.5 <= point <= 3.5:
        sum += 1
print(f'Có {sum} sinh viên có điểm tổng kết trong đoạn [2.5 , 3.5]')

print('----------------------------')
add_key = input('Thêm mã sinh viên: ')
if add_key not in setup_dict:
    add_value = float(input('Thêm điểm tổng kết:'))
    setup_dict[add_key] = add_value
    display()
else:
    print('Đã tồn tại sinh viên trong dict')

print('----------------------------')
xoa_sv = []
for key,value in setup_dict.items():
    if value < 2.0:
        xoa_sv.append(key)
for sv in xoa_sv:
    del setup_dict[sv]
display()