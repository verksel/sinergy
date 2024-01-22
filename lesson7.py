A = 10000 # капитал Майкла
B = 15000 # капитал Иванова
print("Задайте минимальную сумму инвестиций - ")
X = int(input())
if (A >= X) and (B >= X):
    print("2")
elif (A >= X):
    print("Mike")
elif (B >= X):
    print("Ivan")
elif (A+B >= X):
    print("1")
else:
    print("0")