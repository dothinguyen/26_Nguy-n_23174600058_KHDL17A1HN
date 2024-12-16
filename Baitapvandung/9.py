class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh  

class HinhBinhHanh(DaGiac):
    def __init__(self, day, cao):
        super().__init__(4)  
        self.day = day  
        self.cao = cao  

    def dien_tich(self):
        return self.day * self.cao

    def chu_vi(self):
        return 2 * (self.day + self.cao)

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, rong, cao):
        super().__init__(rong, cao)  

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh) 

# --------------------------------------------------------------------------------
rong = float(input("Nhập chiều rộng hình chữ nhật: "))
cao = float(input("Nhập chiều cao hình chữ nhật: "))
hcn = HinhChuNhat(rong, cao)  
print(f"Hình chữ nhật: Chu vi = {hcn.chu_vi()}, Diện tích = {hcn.dien_tich()}")

# ------------------------------------------------------------------------
canh = float(input("Nhập độ dài cạnh hình vuông: "))
hv = HinhVuong(canh) 
print(f"Hình vuông: Chu vi = {hv.chu_vi()}, Diện tích = {hv.dien_tich()}")
