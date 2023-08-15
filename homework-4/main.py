from src.item import Item, nice_number_output
from src.phone import Phone

if __name__ == '__main__':
    # ДОМАШНЕЕ ЗАДАНИЕ 4 по проекту Магазин Электроники
    # НАЧАЛО программы
    #

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    print()
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    print(phone1)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    print(repr(phone1))
    assert phone1.number_of_sim == 2
    print()
    item1 = Item("Смартфон", 10000, 20)
    for item in Item.all:
        print(f'\033[33m{item.name}\033[39m '
              f'в количестве \033[33m{item.quantity} шт.\033[39m '
              f'по цене \033[32m{nice_number_output(item.price)} руб.\033[39m '
              f'Итоговая сумма = '
              f'\033[32m{nice_number_output(item.calculate_total_price())}'
              f' руб.\033[39m')
    print()
    assert item1 + phone1 == 25
    print(f'Количество устройств \033[33m{item1}\033[39m и '
          f'\033[33m{phone1}\033[39m = \033[32m{item1 + phone1}\033[39m')
    assert phone1 + phone1 == 10
    print(f'Количество устройств \033[33m{phone1}\033[39m и '
          f'\033[33m{phone1}\033[39m = \033[32m{phone1 + phone1}\033[39m')
    print()
    print(repr(phone1))
    print()
    print('Создадим новый телефон с количеством симкарт = 0')
    try:
        phone2 = Phone("iPhone 15", 120_000, 5, 0)
    except ValueError as v_err:
        print(f'\033[31m{v_err.args[0]}\033[39m')

    print('Создадим новый телефон с количеством симкарт = 0.1')
    try:
        phone2 = Phone("iPhone 15", 120_000, 5, 0.1)
    except ValueError as v_err:
        print(f'\033[31m{v_err.args[0]}\033[39m')


    print('Установим количество SIM-карт = 0 ')
    try:
        phone1.number_of_sim = 0
    except ValueError as v_err:
        # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
        print(f'\033[31m{v_err.args[0]}\033[39m')

    print('Установим количество SIM-карт = 0.1 ')
    try:
        phone1.number_of_sim = 0.1
    except ValueError as v_err:
        print(f'\033[31m{v_err.args[0]}\033[39m')

    print()
    print('Установим количество SIM-карт = 10 ')
    phone1.number_of_sim = 10
    print(repr(phone1))
    # print(phone1.my_str())
    print()


    #
    # КОНЕЦ программы
    #
