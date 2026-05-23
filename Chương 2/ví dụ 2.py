a = float(input("nhap so thu nhat ="))
b = float(input("nhap so thu hai ="))
c = float(input("nhap so thu ba ="))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print("so lon nhat trong ba so %f, %f va %f la %f" % (a, b, c, max_val))