from src.item import Item

if __name__ == '__main__':
    #
    # НАЧАЛО программы
    #

    item1 = Item("Смартфон", 10000, 20)
    print(repr(item1))
    print(str(item1))
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

    #
    # КОНЕЦ программы
    #
