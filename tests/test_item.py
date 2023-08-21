"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item as my_item
import pytest
import os

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

    # Для шестого домашнего задания
    # Файл ..\src\items-space_upper.csv - поля написаны с большой и маленькой
    #                                     буквы с пробелами справа и слева,
    #                                     значения полей также с пробелами
    my_item.Item.instantiate_from_csv('..\src\items-space_upper.csv')
    assert len(my_item.Item.all) == 5

    my_item.Item.instantiate_from_csv('..\src\items.csv')
    assert len(my_item.Item.all) == 5
    my_item.Item.all[0].name = 'Купи мама телефон'
    assert my_item.Item.all[0].name == 'Купи мама '
    assert my_item.Item.string_to_number('10') == 10
    assert my_item.Item.string_to_number('10.0001') == 10
    assert my_item.Item.string_to_number('123.456789') == 123

    for i in (1, '1', '1.1', 'Hello', (1, 1), {1: 1}):
        with pytest.raises(TypeError):
            temp_result = temp_item + i

    # Для шестого домашнего задания
    # Файл ..\src\item.csv - не существует
    with pytest.raises(FileNotFoundError):
        my_item.Item.instantiate_from_csv('..\src\item.csv')



    # Файл ..\src\items-err.csv - с ошибкой в имени поля
    # Файл ..\src\items-err01.csv - нет одного из полей
    # Файл ..\src\items-err02.csv - нет значений цены и количества
    # Файл ..\src\items-err03.csv - поле цены - не число
    # Файл ..\src\items-err04.csv - поля цены и количества есть, но они пустые
    for csv_name in ['..\src\items-err.csv',
                     '..\src\items-err01.csv',
                     '..\src\items-err02.csv',
                     '..\src\items-err03.csv',
                     '..\src\items-err04.csv']:
        with pytest.raises(my_item.InstantiateCSVError):
            my_item.Item.instantiate_from_csv(csv_name)



def test_nice_number_output():
    assert my_item.nice_number_output(10000000) == '10 000 000'
    assert my_item.nice_number_output(10000000.0111) == '10 000 000.0111'
