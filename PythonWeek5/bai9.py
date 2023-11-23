import random
n = int(input('Nhập số lượng tài khoản: '))

while n < 10 or n > 100000:
    print('Nhập lại')
    n = int(input('Nhập số lượng tài khoản: '))

major = ['CNTT','KHMT', 'KTPM', 'HTTT']

acc = {}
for i in range(n):
    id_sv = 2022606001 + i
    password = random.choice(major) + str(id_sv)
    acc [f"Account {i+1}: "] = {"Username": id_sv, "password":password}

for key, value in acc.items():
    print(key,value)