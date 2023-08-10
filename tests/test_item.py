"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item as my_item
import pytest

def test_class_item():
    # для первого домашнего задания
    temp_item = my_item.Item('Смартфон',100,1)
    assert temp_item.name == 'Смартфон'
    assert int((1-temp_item.pay_rate)*100) == 15
    assert temp_item.__str__() == "Смартфон"
    assert temp_item.__repr__() == "Item('Смартфон', 100, 1)"
    assert temp_item.calculate_total_price() == 100
    temp_item.apply_discount()
    assert temp_item.calculate_total_price() == 85

    # для второго домашнего задания
    temp_item = my_item.Item('Смартфон',100,1)
    temp_item.name = '01234567890123'
    assert temp_item.name == '0123456789'
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
