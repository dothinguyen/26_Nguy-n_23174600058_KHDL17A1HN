import json
import datetime

class GiaoDich:
    def __init__(self):
        self.transactions = []  

    def them_giao_dich(self, transaction_type, amount):
        transaction = {"type": transaction_type, "amount": amount}
        self.transactions.append(transaction) 

    def luu_giao_dich(self):
        current_time = datetime.datetime.now()
        file_name = current_time.strftime("%Y-%m-%d-%H-%M-%S") + ".json"

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.transactions, file, ensure_ascii=False)
        print(f"Tất cả giao dịch đã được ghi vào tệp {file_name}")

def main():
    quan_ly_giao_dich = GiaoDich()  
    number_of_transactions = int(input("Nhập số giao dịch bạn muốn thực hiện: "))

    for _ in range(number_of_transactions):
        transaction_type = input("Nhập loại giao dịch (tiền hoặc vàng): ")
        amount = float(input("Nhập số tiền/giao dịch: "))
        quan_ly_giao_dich.them_giao_dich(transaction_type, amount)  

    quan_ly_giao_dich.luu_giao_dich()

if __name__ == "__main__":
    main()
