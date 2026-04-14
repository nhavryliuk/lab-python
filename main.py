from functions import compare_speed, convert_time, time_to_midnight

def task19():
    v1 = float(input("Введіть швидкість v1 (км/год): "))
    v2 = float(input("Введіть швидкість v2 (м/с): "))

    print("Результат:", compare_speed(v1, v2))


def task20():
    h, m = map(int, input("Введіть час (год хв): ").split())

    result, error = convert_time(h, m)

    if error:
        print(error)
    else:
        print(result)


def task21():
    h, m = map(int, input("Введіть час (ч м): ").split())
    part = input("Введіть половину доби (a/p): ")

    res = time_to_midnight(h, m, part)

    if res:
        print(f"До опівночі: {res[0]} год {res[1]} хв")
    else:
        print("Incorrect time!")


while True:
    print("\n=== МЕНЮ ===")
    print("1 - Завдання 19")
    print("2 - Завдання 20")
    print("3 - Завдання 21")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        task19()
    elif choice == "2":
        task20()
    elif choice == "3":
        task21()
    elif choice == "0":
        break
    else:
        print("Невірний вибір")