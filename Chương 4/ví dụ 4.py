a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

tong = a + b + c

print("Tong =", tong)

dem = 0

while tong > 0:
    cs = tong % 10

    if cs % 2 == 0:
        dem = dem + 1

        tong = tong // 10

print("So chu so chan trong tong la:", dem)