n = int(input())
st = set(map(int,input().split()))
x = int(input())
sum = 0
result = set()
for i in st:
    if sum + i <= x:
        sum += i
        result.add(i)
print(result)


