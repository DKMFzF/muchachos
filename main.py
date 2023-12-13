""" Фаил main """

import Fun


while True:

    stroka = input("Введите строку: ")

    print("__МЕНЮ__")
    print("1. Функция(1)")
    print("2. Функция(2)")
    print("3. Выход")

    menu = input("Введите: ")

    match menu:
        case '1':
            Fun.bold(stroka)
        case '2':
            Fun.itallic(stroka)
        case '3':
            break
        case _:
            print("Что то не то")
            