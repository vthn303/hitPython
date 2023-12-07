class Hiter:
    id = 1000
    def __init__(self,ten, tuoi, gen):
        self.ten = ten
        self.tuoi = tuoi
        self.gen = gen
        Hiter.id += 1
    def nhap():
        print("Nhap thong tin cac hiter")
        ten = input("Nhap ten: ")
        tuoi = input("Nhap tuoi: ")
        gen = input("Nhap gen: ")
        return Hiter(ten, tuoi, gen)
    def __str__(self):
        return "id: " + str(self.id) + " ten: " + self.ten + " tuoi: " + self.tuoi + " gen: " + self.gen

        
    def xuat():
        print("Xuat thong tin cac hiter")
        for hiter in Hiter.dsHiter:
            print(hiter)

class Ban:
    def __init__(self, idBan, tenBan, truongBan: Hiter, thanhVien:list):
        self.idBan = idBan
        self.tenBan = tenBan
        self.truongBan = truongBan
        self.thanhVien = thanhVien
    def nhap():
        print("Nhap thong tin cac ban")
        idBan = input("Nhap id ban: ")
        tenBan = input("Nhap ten ban: ")
        truongBan = input("Nhap truong ban: ")
        thanhVien = []
        print("Nhap thong tin thanh vien:")
        n = int(input("Nhap so luong thanh vien: "))
        for _ in range(n):
            hiter = Hiter.nhap()
            thanhVien.append(hiter)
        return Ban(idBan, tenBan, truongBan, thanhVien)
    def __str__(self):
        return "Ban: id: " + self.idBan + "\nten: " + self.tenBan + "\ntruong: " + str(self.truongBan) + "\nthanh vien: " + str(self.thanhVien)

    def dsHiter(self):
        print("Xuat thong tin danh sach hiter trong ban")
        for i in self.thanhVien:
            print(i)
    def addHiter(self):
        ten = input("Nhap ten hiter: ")
        tuoi = input("Nhap tuoi hiter: ")
        gen = input("Nhap gen hiter: ")
        for i in range(len(self.thanhVien)):
            if self.thanhVien[i].ten == ten:
                print("Hiter da ton tai")
                return
        hiter = Hiter(ten, tuoi, gen)
        self.thanhVien.append(hiter)
    def delHiter(self):
        ten = input("Nhap ten hiter: ")
        for i in range(len(self.thanhVien)):
            if self.thanhVien[i].ten == ten:
                self.thanhVien.pop(i)
                print("Hiter da xoa thanh cong")
                return
        print("Hiter khong ton tai")

dsHiter = []
n = int(input("nhap n hiter: "))
for i in range(n):
    hiter = Hiter.nhap()
    dsHiter.append(hiter)
print("Xuat danh sach hiter")
for i in dsHiter:
    print(i)
m = int(input("nhap m ban: "))
dsBan = []
for i in range(m):
    ban = Ban.nhap()
    dsBan.append(ban)
print("Xuat danh sach ban")
for i in dsBan:
    print(i)



 

    


