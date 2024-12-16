class TamGiac:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        s = self.chu_vi() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, a, b)

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, (a**2 + b**2) ** 0.5)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

# ------------------------------------------------------------------------------------------------------------------------
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
tam_giac = TamGiac(a, b, c)

a_vuong = float(input("Nhập cạnh a của tam giác vuông: "))
b_vuong = float(input("Nhập cạnh b của tam giác vuông: "))
tam_giac_vuong = TamGiacVuong(a_vuong, b_vuong)

a_deu = float(input("Nhập cạnh của tam giác đều: "))
tam_giac_deu = TamGiacDeu(a_deu)

# -------------------------------------------------------------------------------------------------------------------------------
print(f"Tam giác: Chu vi = {tam_giac.chu_vi()}, Diện tích = {tam_giac.dien_tich()}")
print(f"Tam giác vuông: Chu vi = {tam_giac_vuong.chu_vi()}, Diện tích = {tam_giac_vuong.dien_tich()}")
print(f"Tam giác đều: Chu vi = {tam_giac_deu.chu_vi()}, Diện tích = {tam_giac_deu.dien_tich()}")
