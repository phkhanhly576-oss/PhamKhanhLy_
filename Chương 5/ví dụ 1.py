n = int(input("Nhap n = "))
while n <= 0 or n >= 100:
    n = int(input("Nhap lai n = "))
tong = 0
dem = 0
for i in range(n):
    x = float(input("Nhap x = "))
    if x > -1000 and x < -10: 
    tong += x
    dem += 1
if dem > 0:
    tbc = tong / dem
    print("Trung binh cong =", tbc)
else:
    print("Khong co phan tu thoa dieu kien")