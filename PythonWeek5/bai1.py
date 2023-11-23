set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))
if set1 & set2:
    print('Danh sách sinh viên đăng kí học tại 2 bàn là: ', set1&set2)
else:
    print('Không có sinh viên nào đăng kí học tại 2 bàn')
print('Danh sách tổng hợp các sinh viên đã đăng kí của cả hai bàn: ', set1 | set2)
print('Danh sách sinh viên đã đăng kí tại bàn 1 mà không đăng kí tại bàn 2: ',set1 - set2)
print('Danh sách sinh viên đăng kí duy nhất 1 bàn: ', set1 ^ set2)