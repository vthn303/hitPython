a = input().split()
dicts = {}
for key in a:
    if key in dicts:
        dicts[key] += 1 # tăng value
    else:
        dicts[key] = 1 # nếu không thì value = 1
kq = []
for key, value in dicts.items():
    if value == max(dicts.values()):
        kq.append((key,value))

print(tuple(kq))