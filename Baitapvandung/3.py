class PS:
    def __init__(self):
        self.nhap_phan_so()

    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            return False
        return True

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        if not self.kiem_tra_hop_le():
            print("Mẫu số không được bằng 0. Nhập lại.")
            self.nhap_phan_so()  # Kiểm tra
    def in_phan_so(self):
        print(f"Phân số: {self.tu_so}/{self.mau_so}")


# -------------------------------------------------------------
ps = PS()  
ps.in_phan_so()  
