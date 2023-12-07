class Pycon:
    id = 0

    def __init__(self, hoTen, tuoi):
        Pycon.id += 1
        self.hoTen = hoTen
        self.tuoi = tuoi

    def nhap(self):
        self.hoTen = input()
        self.tuoi = int(input())

    def __str__(self):
        return "ID: {} || Tên: {} || Tuổi: {}".format(Pycon.id, self.hoTen, self.tuoi)

    @classmethod
    def averAge(cls, pycons):
        sumAge = 0
        for pycon in pycons:
            sumAge += pycon.tuoi
        return sumAge / len(pycons)
        

n = int(input("Nhập số lượng Pycon: "))
listAge = []
for _ in range(n):
    pycon = Pycon("", 0)
    pycon.nhap()
    listAge.append(pycon)
    print(pycon)

print("Trung bình tuổi: ", pycon.averAge(listAge))
