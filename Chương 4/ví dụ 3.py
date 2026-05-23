x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
z = int(input("Nhap z: "))

tich = x * y * z  

print("Tich =", tich)

dem = 0
maxx = 0

while tich > 0:
    cs = tich % 10

    dem = dem + 1

    if cs > maxx
       maxx = cs

    tich = tich // 10

print ("So chu so =", dem)
print ("Chu so lon nhat =", maxx)
