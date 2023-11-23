set_input = set(map(int,input().split()))

if 11 not in set_input:
    set_input.add(11)

for i in set_input:
    print(i)
kq = []

for i in range(0, len(set_input) -1):
    for j in range(i+1, len(set_input)):
        if set_input(i) + set_input(j) == 11:
            kq.append((set_input(i),set_input(j)))
            
print(tuple(kq))