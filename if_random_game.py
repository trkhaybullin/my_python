import random

rand_number = random.randint(1, 4)
user_number = int(input("Введите число: "))

if user_number == rand_number:
    print("Победа")
else:
    print("Повторите еще раз")
