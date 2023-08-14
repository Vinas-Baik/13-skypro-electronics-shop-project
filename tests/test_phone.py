import src.phone as my_phone
import src.item as my_item
import pytest


def test_class_phone():
    temp_phone = my_phone.Phone('Смартфон', 100)
    assert temp_phone.number_of_sim == 1
    assert temp_phone.quantity == 1
    temp_phone = my_phone.Phone('Смартфон', 100, 10, 2)
    assert temp_phone.number_of_sim == 2
    assert temp_phone.quantity == 10
    temp_phone.name = '01234567890123456789'
    assert temp_phone.name == '0123456789'
    assert repr(temp_phone) == "Phone('0123456789', 100, 10, 2)"
    temp_item = my_item.Item('Смартфон',100,5)
    assert temp_phone + temp_item == 15
    try:
        temp_phone.number_of_sim == -1
    except ValueError as v_err:
        assert v_err.args[0] == 'Количество физических SIM-карт должно быть целым числом больше нуля'
    try:
        temp_phone.number_of_sim == 0.1
    except ValueError as v_err:
        assert v_err.args[0] == 'Количество физических SIM-карт должно быть целым числом'

def test_class_item():
    # для первого домашнего задания
    temp_item = my_item.Item('Смартфон',100,1)
    assert temp_item.name == 'Смартфон'
    assert int((1-temp_item.pay_rate)*100) == 15
    assert temp_item.__str__() == "Смартфон"
    assert temp_item.__repr__() == "Item('Смартфон', 100, 1)"
    assert temp_item.my_str() == "Смартфон в количестве 1 шт по цене 100 руб. - итоговая сумма 100 руб."

    assert temp_item.calculate_total_price() == 100
    temp_item.apply_discount()
    assert temp_item.calculate_total_price() == 85

    # для второго домашнего задания
    temp_item = my_item.Item('Смартфон',100,5)
    temp_item.name = '01234567890123'
    assert temp_item.name == '0123456789'
    assert temp_item+temp_item == 10
    # assert temp_item+1 == TypeError('ошибка типов')

    my_item.Item.instantiate_from_csv()
    assert len(my_item.Item.all) == 5
    my_item.Item.all[0].name = 'Купи мама телефон'
    assert my_item.Item.all[0].name == 'Купи мама '
    assert my_item.Item.string_to_number('10') == 10
    assert my_item.Item.string_to_number('10.0001') == 10
    assert my_item.Item.string_to_number('123.456789') == 123


def test_nice_number_output():
    assert my_item.nice_number_output(10000000) == '10 000 000'
    assert my_item.nice_number_output(10000000.0111) == '10 000 000.0111'