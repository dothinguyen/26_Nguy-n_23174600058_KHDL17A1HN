class HinhChuNhat:
    def __init__(self):
        self.chieu_dai = float(input("Nhập chiều dài: "))
        self.chieu_rong = float(input("Nhập chiều rộng: "))

    def chu_vi(self):
        return 2 * (self.chieu_dai + self.chieu_rong)

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def thong_tin(self):
        return (f"Dài: {self.chieu_dai}, Rộng: {self.chieu_rong}, "
                f"Chu vi: {self.chu_vi()}, Diện tích: {self.dien_tich()}")
#---------------------------------------------------------------------------
hcn = HinhChuNhat()
print(hcn.thong_tin())
