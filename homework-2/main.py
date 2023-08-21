from src.item import Item

if __name__ == '__main__':
    print('\n1 часть задания:\n')

    item = Item('Телефон', 10000, 5)
    print(item)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    print(item)

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    print(item)
    assert item.name == 'СуперСмарт'

    item.name = '01234567890123456789'
    # Exception: Длина наименования товара превышает 10 символов.
    print(item)

    assert item.name == '0123456789'

    print('\n2 часть задания:\n')

    Item.instantiate_from_csv('..\src\items.csv')  # создание объектов из данных файла
    print(Item.all)
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

    print('\n3 часть задания:\n')

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    print(Item.string_to_number('5'))
    print(Item.string_to_number('5.0'))
    print(Item.string_to_number('5.5'))
