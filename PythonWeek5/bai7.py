a = input()
dicts ={}
for key in a:
    if key in dicts:
        dicts[key] += 1
    else:
        dicts[key] = 1
print(dicts)