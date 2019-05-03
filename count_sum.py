num = input("Введите число: ")
total = 0
for i in num:
    if int(i)%2 != 0:
        total += pow(int(i), 2)
    
print("Результат:", total)
