cnt = 0
n = int(input())
str = list(map(int,input().split()))
while len(str) != n:
  if(len(str) > n):
    print(f'nhap lai {n} so')
    str = list(map(int,input().split()))
result = []
for i in str:
  mod = i % 10
  if mod == 1 or mod == 3 or mod == 5 or mod == 7 or mod == 9:
    cnt += 1
    result.append(i)
result.sort()
print (cnt)
for i in result:
  print(i, end = " ")
print()
    



