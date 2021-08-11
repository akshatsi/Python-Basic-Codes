a = int(input("enter"))
total = 0
while (a > 0):
    total = total + (a % 10)
    a = a // 10
print(total)
