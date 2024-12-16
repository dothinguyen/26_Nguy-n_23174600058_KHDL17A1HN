class TS:
    def __init__(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"{self.ho_ten}: Tổng điểm = {self.tong_diem()}")



n = int(input("Nhập số lượng thí sinh: "))
danh_sach = [TS() for _ in range(n)]  

print("\nDanh sách thí sinh trúng tuyển (điểm chuẩn 20):")
for ts in sorted(danh_sach, key=lambda x: x.tong_diem(), reverse=True):
    if ts.tong_diem() >= 20:
        ts.in_thong_tin()