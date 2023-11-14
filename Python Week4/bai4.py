n = int(input())
str = list(map(int,input().split()))
while len(str) != n:
  if(len(str) > n):
    print(f'nhap lai {n} so')
    str = list(map(int,input().split()))
odd = 0
even = 0
for i in str:
  if i % 2 == 0:
    even += 1
  else:
    odd += 1
if even > odd :
  print('even')
elif even < odd:
  print('odd')
else:
  print('equal')

