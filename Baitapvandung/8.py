class Date:
    def __init__(self, day=1, month=1, year=2023):
        self.day, self.month, self.year = day, month, year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

class Employee:
    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    def display_info(self):
        print(f"Họ tên: {self.name}, Ngày sinh: ", end="")
        self.birth_date.display()
        print("Ngày vào công ty: ", end="")
        self.start_date.display()
#-------------------------------------------------------------------
employees = []
for _ in range(int(input("Nhập số lượng nhân viên: "))):
    name = input("Nhập họ tên: ")
    birth_date = Date(int(input("Ngày sinh: ")), int(input("Tháng sinh: ")), int(input("Năm sinh: ")))
    start_date = Date(int(input("Ngày vào công ty: ")), int(input("Tháng vào công ty: ")), int(input("Năm vào công ty: ")))
    employees.append(Employee(name, birth_date, start_date))
for emp in employees:
    emp.display_info()
    print()
