sogiolam = float(input("Nhap so gio lam moi tuan "))
luonggio = float(input("Nhap thu lap tren moi gio lam tieu chuan "))
giotieuchuan = 44 # So gio lam chuan moi tuan 
giovuotchuan = max(0, sogiolam - giotieuchuan) # So gio lam vuot chuan moi tuan
thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5 # Tinh tong thu nhap
print(f"So tien thuc lich cua nhan vien : {thuclinh}") 