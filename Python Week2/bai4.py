a = int(input('nhập 1 số bất kì: '))

a_abs = abs(a)
count = a_abs.bit_length()
#số lượng các bits cần thiết để biểu diễn số a ở dạng nhị phân, không bao gồm phần dấu và các số 0 ở đầu.
print(count)

#Kiểm tra danh sách các thuộc tính và phương thức hiện tại của một biến có kiểu dữ liệu là number.
print(dir(a))