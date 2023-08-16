import src.keyboard as my_kb
import src.item as my_item
import pytest


def test_class_phone():
    temp_kb = my_kb.Keyboard('Logitech', 2000, 5)
    assert temp_kb.language == 'EN'
    assert repr(temp_kb) == "Keyboard('Logitech', 2000, 5, EN)"
    with pytest.raises(ValueError):
        temp_kb = my_kb.Keyboard('Logitech', 2000, 5, 'СH')

    temp_kb = my_kb.Keyboard('Logitech', 2000, 10, 'RU')
    assert temp_kb.language == 'RU'
    assert temp_kb.change_lang().language == 'EN'
    assert temp_kb.change_lang().change_lang().language == 'EN'
    assert temp_kb.my_str() == 'Logitech в количестве 10 шт по цене 2 000 руб. ' \
                               '- итоговая сумма 20 000 руб., установлен язык - EN'