from src.item import Item
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
    print(item1.my_str())
    print(phone1.my_str())
    print()
    assert item1 + phone1 == 25
    print(f'Количество устройств {item1} и {phone1} = {item1 + phone1}')
    assert phone1 + phone1 == 10
    print(f'Количество устройств {phone1} и {phone1} = {phone1 + phone1}')
    print()
    print(repr(phone1))
    print()

    print('Установим количество SIM-карт = 0 ')
    try:
        phone1.number_of_sim = 0
    except ValueError as v_err:
        # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
        print(v_err.args[0])

    print('Установим количество SIM-карт = 0.1 ')
    try:
        phone1.number_of_sim = 0.1
    except ValueError as v_err:
        print(v_err.args[0])

    print()
    print('Установим количество SIM-карт = 10 ')
    phone1.number_of_sim = 10
    print(repr(phone1))
    # print(phone1.my_str())
    print()


    #
    # КОНЕЦ программы
    #
