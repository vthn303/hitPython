championLOL = ["Yasuo", "Lee Sin", "Zed", "Master Yi", "Garen", "Tryndamere"]
dataLOL = [
    {"price": 6300, "Ulti": "Trăn trối"},
    {"price": 4800, "Ulti": "Nộ Long Cước"},
    {"price": 4800, "Ulti": "Dấu Ấn Tử Thần"},
    {"price": 450, "Ulti": "Chiến Binh Sơn Cước"},
    {"price": 450, "Ulti": "Công Lý Demacia"},
    {"price": 1350, "Ulti": "Từ Chối Tử Thần"}	
]

dicts = {}

for i in range(len(championLOL)):
    dicts[championLOL[i]] = dataLOL[i]

print(dicts)

s = input()
if s in dicts.keys():
    print(dicts[s]["price"])
else:
    print('khong co phan tu nay trong dict')