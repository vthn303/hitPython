a = int(input('nhap a = '))
b = int(input('nhap b = '))

print('a + b = ' , a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ',(int) (a / b))
print('a^b = ', a ** b)
print('a mod b = ', a % b)
if a > b:
    print(f'{a} lớn hơn {b}')
elif a < b :
    print(f'{a} nhỏ hơn {b}')
else:
    print(f'{a} bằng {b}')
print('a AND b =', a & b)
print('a OR b = ', a | b)
print('a XOR b = ', a^b)
print("NOT a==b : ", not a==b)
print('a dịch phải 5 bit = ', a >> 5)
print('a dịch trái 6 bit = ', a << 6) 
print(f'hệ cơ số 2 đảo ngược của {a} là: ',bin(a)[2:][::-1])

