value = input("Введите № элемента: ")
if value:
    Li = int(value)
    Mn = int(value)
    Hg = int(value)
    Cl = int(value)
    if Li == 3:
        print("Литий - Li")
    elif Mn == 25:
        print("Марганец - Mn")
    elif Hg == 80:
        print("Ртуть - Hg")
    elif Cl == 17:
        print("Хлор - Cl")
    else:
        print("Что это?!")
else:
    print("Введите значение элемента!")
