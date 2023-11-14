a = input()
sum = 0
i = 0
while i < len(a):
    if '0' <= a[i] <= '9':
        flag = 1
        tmp = int(a[i])
        if i > 0 and a[i - 1] == '-':
            flag = -1
        j = i + 1
        while j < len(a) and '0' <= a[j] <= '9':
            tmp *= 10
            tmp += int(a[j])
            j += 1
            i += 1
        sum += tmp * flag
    i += 1
print(sum)
