import datetime
now = datetime.datetime.now() 
print(now)
S = now.strftime("%d/%m/%Y, %H:%M:%S") # 
print("S:", S)