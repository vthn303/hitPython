n = int(input())
a = [input() for i in range (n)]
b = tuple(a)
print(b)
cnt = 0
for i in range(len(b)):
    if b[i].isdigit():
        cnt +=1
print(f'Có {cnt} phần tử trong b có dạng số')
