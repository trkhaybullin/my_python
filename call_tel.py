def call_tel(num1, num2):
    if num1 == 343:
        return num2 * 15
    elif num1 == 381:
        return num2 * 18
    elif num1 == 473:
        return num2 * 13
    elif num1 == 485:
        return num2 * 11
num1 = int(input("Введите код города: "))
num2 = int(input("Введите длительность разговора: "))
print("Стоимость разговора:", call_tel(num1, num2), "рублей")

