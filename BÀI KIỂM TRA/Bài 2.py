# Nhập số nguyên dương n
n = int(input("Nhập vào số nguyên dương n: "))
tong_chu_so = sum(int(chuyen_doi) for chuyen_doi in str(n))
print (f"Tổng các chữ số của {n} là : {tong_chu_so}")
# Kiểm tra chia hết cho 3
if tong_chu_so % 3 == 0:
    print ("Tổng các chữ số của n chia hết cho 3")
else :
    print ("Tổng các chữ số không chia hết cho 3")