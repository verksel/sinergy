print("Введите пятизначное число -")
num = int(input())
dt = num // 10000
ts = (num % 10000) // 1000
sot = ((num % 10000) % 1000) // 100
des = (((num % 10000) % 1000) % 100) // 10
ed = (((num % 10000) % 1000) % 100) % 10
# print(dt, ts, sot, des, ed, sep="+")
print(((des ** ed) * sot) / (dt - ts))
