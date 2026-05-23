n = int(input("Nhap n = "))
while n <= 0 or n >= 200:
    n = int(input("Nhap lai n = "))
tong = 0
for i in range(n):
    x = int(input("Nhap x = "))
    if x % 2 == 0:
        tong = tong + x
print("Tong cac phan tu chan =", tong)
if tong % 7 == 0 and tong < 200:
    print("Tong thoa dieu kien")
else:
    print("Tong khong thoa dieu kien")