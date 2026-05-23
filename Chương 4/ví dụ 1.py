n = int(input("Nhap n = "))
while n > 100 or n < 0:
    n = int(input("Nhap n (0 < n < 100): "))
tong = 0
for i in range(n):
    X = int(input("Nhap phan tu thu %d: " % (i + 1)))
    kt = True
    if X < 2 :
        kt = False
    else:
        for j in range(2, int(X ** 0.5) + 1):
            if X % j == 0:
                kt = False
            if kt == True:
                tong = tong + X
print ("Tong cac so nguyen to la: ", tong)
if tong % 2 != 0 and tong > 50:
    print ("Tong la so le va lon hon 50")
else:
    print ("Tong khong la so le va lon hon 50")