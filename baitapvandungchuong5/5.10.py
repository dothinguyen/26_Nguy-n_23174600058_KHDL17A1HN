import sqlite3
conn = sqlite3.connect(r'D:\baitapvandungchuong5\product.db')
curso = conn.cursor()

def hien_thi():
    rows =curso.execute("SELECT * FROM product")
    print("danh sach san pham la: ")
    for row in rows:
        print(row)
def them_san_pham():
    name = input("nhap san pham muon them: ")
    price = int(input("nhap gia cua san pham: "))
    amount = int(input("nhap so luong san pham: "))
    curso.execute("""INSERT INTO product ('Name','Price','Amount') VALUES
                    (?,?,?)""",(name,price,amount))
    conn.commit()
    print("Sản phẩm đã được thêm thành công.")

def tim_kiem(name):
    rows =curso.execute("SELECT * FROM product WHERE Name = ?",(name,))
    for row in rows:
        print(row) 
def cap_nhat(id,price,amount):
    curso.execute(f"UPDATE product SET Price = ?, Amount =? WHERE id = ?",(price,amount,id))
    conn.commit()
    print("Cập nhật sản phẩm thành công.")
def xoa(id):
    curso.execute(f"DELETE FROM product WHERE id = ?",(id,))
    conn.commit()
    print("Sản phẩm đã được xóa thành công.")

def main():
    print("==================================")
    print("==== Chuong trinh quan ly san phan ====")
    print("\nNhập lựa chọn:")
    print("  0: Hiển thị danh sách sản phẩm")
    print("  1: Thêm sản phẩm")
    print("  2: Tìm kiếm sản phẩm")
    print("  3: Cập nhật đơn giá và số lượng")
    print("  4: Xóa sản phẩm")
    while True:
        try:
            hoi = int(input())
        except ValueError:
            print("vui long nhap so tu 0 den 4")
            continue
        if hoi == 0:    
            hien_thi()
        elif hoi ==1:
            them_san_pham()
        elif hoi ==2:
            name = input("nhap ten san pham muon tim: ")
            tim_kiem(name)
        elif hoi ==3:
            id = int(input("nhap id san pham muon cap nhat: "))
            price = int(input("nhap gia muon cap nhat: "))
            amount = int(input("nhap so luong muon cap nhat: "))
            cap_nhat(id,price,amount)
        elif hoi ==4:
            id = int(input("nhap id san pham muon xoa: "))
            xoa(id)
        else:
            print("chuong trinh nhap khong hop le")
        tt = input("ban co muon tiep tuc chuong trinh? (Y/N): ")
        if tt.lower() == 'n':
            print("chuong trinh ket thuc !!!!!")
            break
if __name__ == "__main__":
    main()