s = input()
str = s.split('/')
str_int = [int(x) for x in str]
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_ip = month[str_int[1]-1]
day1 = month_ip - str_int[0] + 1
day2 = 0
if((str_int[2] % 4 == 0 and str_int[2] % 100 != 0) or (str_int[2] % 400 == 0)):
    month[1] += 1
for i in range(str_int[1],len(month)):
    day2 += month[i]
result = day1 + day2
print(result)



